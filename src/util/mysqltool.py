import aiomysql
from config.settings import DATABASE_CONFIG

class MySQLTool():
    def __init__(self) -> None:
        self.conn = None
        self.cursor = None
        self.initialized = False

    async def init_connect(self):
        c = DATABASE_CONFIG['dev']
        self.pool = await aiomysql.create_pool(host=c["host"], 
                                            port=c["port"],
                                            user=c["user"], 
                                            password=c["password"],
                                            db=c["database"])
        self.conn = await self.pool.acquire()
        self.cursor = await self.conn.cursor()
        self.initialized = True

    async def ensure_initialized(self):
        if not self.initialized:
            await self.init_connect()
    
    async def close(self):
        if self.conn is not None:
            self.conn.close()
        if self.pool is not None:
            await self.pool.close()

    # 执行SQL语句
    async def execute_sql(self, sql: str) -> int:
        await self.ensure_initialized()
        rows  = await self.cursor.execute(sql)
        # self.conn.commit()
        return rows

    # 执行插入SQL语句
    async def execute_insert(self, sql: str) -> int:
        await self.ensure_initialized()
        rows  = await self.cursor.execute(sql)
        return rows
    
    # 执行获取单条数据SQL语句
    async def execute_fetchone(self, sql):
        await self.ensure_initialized()
        await self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data

    # 执行获取所有数据SQL语句
    async def execute_fetchall(self, sql: str) -> list:
        await self.ensure_initialized()
        await self.cursor.execute(sql)
        data =  await self.cursor.fetchall()
        return data
