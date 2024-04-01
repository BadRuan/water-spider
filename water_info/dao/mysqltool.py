import pymysql
from config.settings import DATABASE_CONFIG

class MySQLTool(object):
    def __init__(self) -> None:
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

    def close(self) -> None:
        self.connection.close()
