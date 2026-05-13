from typing import List, Any, Optional
from itertools import batched
from asyncpg import connect
from settings import postgres
from model import Request
from utils.logger import Logger


log = Logger(__name__)

class Storage():   
    def __init__(self) -> None:
        self.connection = None
        self.initialized = None
    
    async def __aenter__(self):
        await self.ensure_initialized()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            await self.connection.close()
    
    async def ensure_initialized(self):
        if self.initialized is None:
            await self.init_connect()
            
    async def init_connect(self):
        self.connection = await connect(host=postgres.url, user=postgres.user, password=postgres.password, port=postgres.port, database=postgres.database, server_settings={
            'timezone': 'UTC'  # 设置时区，例如 'UTC' 或 'Asia/Shanghai'
        })
                   
    async def query_one(self, sql: str) -> Optional[Any]:
        if self.connection is not None:
            result = await self.connection.fetchrow(sql)
            if result is None:
                return None
            else:
                return result
        else:
            return None
        
    async def query_list(self, sql: str) -> List[Any]:
        if self.connection is not None:
            return await self.connection.fetch(sql)
        else:
            return []
    
    async def save(self, sql: str) -> int:
        if self.connection is not None:
            return await self.connection.execute(sql)
        else:
            return 0
    
    async def insert_waterlevel(self, request: Request):
        SQL = f"""INSERT INTO station_{request.code} (ts, height)
                VALUES"""

        if len(request.data) > 0:
            for wateritem_list in batched(request.data, n=1000):
                sql = SQL
                for water_item in wateritem_list:
                    sql += f"('{water_item.timestamp}', {water_item.height}),"
                sql= sql[:-1] + " ON CONFLICT (ts) DO NOTHING;"
                await self.save(sql)

    async def get_total_count(self) -> int:
        sql: str = 'select count(*) from station;'
        result = await self.query_one(sql)
        if result == None:
            return 0
        else:
            return int(result[0])

async def recoder_count_change(func):
    async def wrap(*args, **kwargs):
        async with Storage() as storage:
            old_count: int = await storage.get_total_count()
            result = func(*args, **kwargs)
            new_count: int = await  storage.get_total_count()
            change_int: int = new_count - old_count
            log.info(f"实际新增 {change_int} 条水位数据")
            return result
    return wrap
        