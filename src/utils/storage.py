from typing import List
from itertools import batched
from psycopg2 import connect as pq_connect
from model import WaterItem, Request
from utils.logger import Logger
from settings import postgres


log = Logger(__name__)


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
        
        
    def query_one(self, sql: str):
        self.execute()
        if self.cursor is not None:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        else:
            return ''
        
    def query_all(self, sql: str) -> List:
        self.execute()
        if self.cursor is not None:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            return []
    
    def insert_waterlevel(self, request: Request):
        SQL = f"""INSERT INTO station_{request.code} (ts, height)
                VALUES"""

        if len(request.data) > 0:
            for wateritem_list in batched(request.data, n=1000):
                sql = SQL
                for water_item in wateritem_list:
                    sql += f"('{water_item.timestamp}', {water_item.height}),"
                sql= sql[:-1] + " ON CONFLICT (ts) DO NOTHING;"
                self.save(sql)

    def get_total_count(self) -> int:
        sql: str = 'select count(*) from station;'
        result = self.query_one(sql)
        if result == None:
            return 0
        else:
            return int(result[0])

def recoder_count_change(func):
    def wrap(*args, **kwargs):
        with PostgresStorage() as storage:
            old_count: int = storage.get_total_count()
            result = func(*args, **kwargs)
            new_count: int = storage.get_total_count()
            change_int: int = new_count - old_count
            log.info(f"实际新增 {change_int} 条水位数据")
            return result
    return wrap
        