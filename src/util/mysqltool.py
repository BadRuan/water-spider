import logging
import pymysql
from config.settings import DATABASE_CONFIG

# 单例模式
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MySQLTool(metaclass=Singleton):
    def __init__(self) -> None:
        try:
            c = DATABASE_CONFIG['dev']
            self.connection = pymysql.connect(
                host=c["host"],
                user=c["user"],
                password=c["password"],
                port=c["port"],
                database=c["database"],
                charset = 'utf8',
                cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()
        except self.connection.Error as err:
            logging.error(f"MySQL连接错误: {err}")
            raise ConnectionError(err)

    def execute(self, sql: str) -> int:
        rows  = self.cursor.execute(sql)
        self.connection.commit()
        return rows

    # 执行插入语句SQL语句
    def execute_insert(self, sql: str) -> int:
        rows  = self.cursor.execute(sql)
        self.connection.commit()
        return rows
    
    # 执行获取单条数据SQL语句
    def execute_fetchone(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data

    # 执行获取所有数据SQL语句
    def execute_fetchall(self, sql: str) -> list:
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def __del__(self) -> None:
        self.connection.close()
