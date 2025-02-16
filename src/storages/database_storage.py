import taosws
from typing import List
from model import DatabaseConfig, DataWaterlevel, WaterLevel
from config.configuration import getDatabase
from utils.logger import Logger


logger = Logger(__name__)


class DatabaseStorage:
    def __init__(self) -> None:
        self.conn = None
        self.initialized = False

    def init_connect(self):
        try:
            _dbc: DatabaseConfig = getDatabase()
            dsn = f"taosws://{_dbc.user}:{_dbc.password}@{_dbc.url}:{_dbc.port}"
            self.conn = taosws.connect(dsn)
            self.conn.execute(f"USE {_dbc.database}")
            logger.info("数据库已连接")
            self.initialized = True
        except Exception:
            logger.error(f"数据库异常: {Exception}")

    def ensure_initialized(self):
        if not self.initialized:
            self.init_connect()

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.conn is not None:
            self.conn.close()
            logger.info("数据库已断开")

    def __enter__(self):
        self.ensure_initialized()
        return self

    def query(self, sql):
        self.ensure_initialized()
        return self.conn.query(sql)

    def insert_waterlevel(self, data_waterlevel: DataWaterlevel):
        # 防止数据过多拼接sql语句过长，对数据进行切片处理
        def slice_list(data: List, length: int = 1000):
            return [data[i : i + length] for i in range(0, len(data), length)]

        SQL = f"""INSERT INTO t{data_waterlevel.stcd}
                USING waterlevel TAGS({data_waterlevel.stcd}, '{data_waterlevel.name}')
                VALUES"""

        slice_data: List[WaterLevel] = slice_list(data_waterlevel.data)

        for waterlevel_list in slice_data:
            sql = SQL
            for waterlevel in waterlevel_list:
                sql += f"('{waterlevel.tm}:00.000', {waterlevel.z})"

            self.query(sql)
