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
        result = await conn.fetchrow(sql)
        if result is None:
            return None
        else:
            return result
    
        
async def query_list( sql: str) -> List[Any]:
    async with get_db_connection() as connection:
        if connection is not None:
            return await connection.fetch(sql)
        else:
            return []
    
async def save( sql: str) -> int:
    async with get_db_connection() as connection:
        if connection is not None:
            return await connection.execute(sql)
        else:
            return 0
    
async def insert_waterlevel( request: Request):
    SQL = f"""INSERT INTO station_{request.code} (ts, height)
                VALUES"""
    if len(request.data) > 0:
        for wateritem_list in batched(request.data, n=1000):
            sql = SQL
            for water_item in wateritem_list:
                sql += f"('{water_item.timestamp}', {water_item.height}),"
            sql= sql[:-1] + " ON CONFLICT (ts) DO NOTHING;"
            await save(sql)

async def get_total_count() -> int:
    sql: str = 'select count(*) from station;'
    result = await query_one(sql)
    if result == None:
        return 0
    else:
        return int(result[0])

async def recoder_count_change(func):
    async def wrap(*args, **kwargs):
        old_count: int = await get_total_count()
        result = func(*args, **kwargs)
        new_count: int = await get_total_count()
        change_int: int = new_count - old_count
        log.info(f"实际新增 {change_int} 条水位数据")
        return result
    return wrap
        