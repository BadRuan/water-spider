import taosrest
from config.settings import DATABASE_CONFIG


class TDengineTool:
    def __init__(self) -> None:
        self.conn = None
        self.initialized = False

    def init_connect(self):
        try:
            c = DATABASE_CONFIG["dev"]
            self.conn = taosrest.connect(
                url=c["url"],
                user=c["user"],
                password=c["password"],
                database=c["database"],
            )
            self.initialized = True
        except taosrest.Error as e:
            print(e)
            print("exception class: ", e.__class__.__name__)
            print("error number:", e.errno)
            print("error message:", e.msg)
        except BaseException as other:
            print("exception occur")
            print(other)

    def ensure_initialized(self):
        if not self.initialized:
            self.init_connect()

    def close(self):
        if self.conn is not None:
            self.conn.close()

    # 执行SQL语句
    async def execute_sql(self, sql: str) -> int:
        self.ensure_initialized()
        return self.conn.execute(sql)

    # 执行获取数据SQL语句
    async def execute_fetch(self, sql):
        self.ensure_initialized()
        return self.conn.execute(sql)
