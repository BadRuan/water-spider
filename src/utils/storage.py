from typing import List
from psycopg2 import connect as pq_connect
from model import WaterItem, Station
from settings import postgres


class PostgresStorage():   
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.initialized = None
    
    def __enter__(self):
        self.ensure_initialized()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
   
    
    def ensure_initialized(self):
        if self.initialized is None:
            self.init_connect()
            
    def execute(self) -> None:
        self.ensure_initialized()


    def init_connect(self):
        self.connection = pq_connect(host=postgres.url, user=postgres.user, password=postgres.password, port=postgres.port, database=postgres.database)
        if self.connection is not None:    
            self.cursor = self.connection.cursor()
              
    def save(self, sql: str) -> None:
        self.execute()
        if self.cursor is not None and self.connection is not None:
            self.cursor.execute(sql)
            self.connection.commit()
        
    def query(self, sql: str) -> List:
        self.execute()
        if self.cursor is not None:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            return []
    
    def insert_waterlevel(self, station: Station):
        # 防止数据过多拼接sql语句过长，对数据进行切片处理
        def slice_list(data: List, length: int = 1000):
            return [data[i : i + length] for i in range(0, len(data), length)]

        SQL = f"""INSERT INTO station_{station.code} (ts, height)
                VALUES"""

        if len(station.water_items) > 0:

            slice_data: List[WaterItem] = slice_list(station.water_items) # type: ignore
            
            for wateritem_list in slice_data:
                sql = SQL
                for water_item in wateritem_list: # type: ignore
                    sql += f"('{water_item.timestamp}', {water_item.height}),"
                sql= sql[:-1] + "ON CONFLICT (ts) DO NOTHING;"
                self.save(sql + ";")