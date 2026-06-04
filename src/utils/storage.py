import re
from datetime import datetime
from typing import List, Any, Optional
from itertools import batched
from asyncpg import create_pool, Pool
from contextlib import asynccontextmanager
from src.settings import settings
from src.model import Request
from src.utils.logger import Logger


log = Logger(__name__)

_db_pool: Optional[Pool] = None


async def init_db_pool():
    """应用启动时调用，初始化全局连接池"""
    global _db_pool
    if _db_pool is None:
        async def set_timezone(connection):
            await connection.execute(f"SET TIME ZONE '{settings.TIMEZONE}';")

        _db_pool = await create_pool(
            dsn=settings.DATABASE_URL,
            min_size=2,          # 最小连接数
            max_size=20,         # 最大连接数，根据实际并发量调整
            init=set_timezone,   # 初始化连接时的回调
            max_inactive_connection_lifetime=300.0 # 空闲连接回收时间
        )

async def close_db_pool():
    """应用关闭时调用，释放连接池资源"""
    global _db_pool
    if _db_pool:
        await _db_pool.close()
        _db_pool = None

@asynccontextmanager
async def get_db_connection():
    """获取连接的上下文管理器，从全局池中借用和归还连接"""
    if not _db_pool:
        raise RuntimeError("数据库连接池未初始化，请先调用 init_db_pool()")

    async with _db_pool.acquire() as conn:
        yield conn

async def query_one(sql: str) -> Optional[Any]:
    async with get_db_connection() as conn:
        return await conn.fetchrow(sql)

async def query_list(sql: str) -> List[Any]:
    async with get_db_connection() as conn:
        return await conn.fetch(sql)

async def save(sql: str) -> int:
    async with get_db_connection() as conn:
        return await conn.execute(sql)

# 允许的表名模式：station_ 后跟纯数字
_TABLE_NAME_PATTERN = re.compile(r'^station_\d+$')

def _validate_table_name(table_name: str) -> str:
    """校验表名，防止 SQL 注入"""
    if not _TABLE_NAME_PATTERN.match(table_name):
        raise ValueError(f"非法的表名: {table_name}")
    return table_name

async def insert_waterlevel(request: Request):
    """使用参数化查询插入水位数据，防止 SQL 注入"""
    if not request.data:
        return

    table_name = _validate_table_name(f"station_{request.code}")
    sql = f"INSERT INTO {table_name} (ts, height) VALUES ($1, $2) ON CONFLICT (ts) DO NOTHING;"

    async with get_db_connection() as conn:
        for wateritem_list in batched(request.data, n=1000):
            # 转换为 asyncpg 要求的原生类型：timestamp → datetime, height → float
            records = [
                (datetime.strptime(item.timestamp, "%Y-%m-%d %H:%M"), float(item.height))
                for item in wateritem_list
            ]
            await conn.executemany(sql, records)

async def get_total_count() -> int:
    sql = 'SELECT count(*) FROM station;'
    result = await query_one(sql)
    if result is None:
        return 0
    return int(result[0])
