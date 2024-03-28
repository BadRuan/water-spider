import pymysql

class MySQLTool(object):
    def __init__(self,host: str, user: str, password: str, port: int, database: str) -> None:

        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             port=port,
                             database=database,
                             charset = 'utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    # 执行插入语句SQL语句
    def __execute_insert(self, sql: str) -> int:
        rows  = self.cursor.execute(sql)
        self.connection.commit()
        return rows
    
    # 执行获取单条数据SQL语句
    def __execute_fetchone(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    # 执行获取所有数据SQL语句
    def __execute_fetchall(self, sql: str) -> list:
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    # 插入水位站点代码
    def insert_station(self, STCD: int, NAME: str) -> int:
        SQL = "INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (`%s`, '%s')" % (STCD, NAME)
        return self.__execute_insert(SQL)
    
    # 插入某条水位数据
    def insert_water_level(self, STCD: int, Z: float, TM: str) -> int:
        SQL = "INSERT INTO `water_level` (`STCD`, `Z`, `TM`) VALUES (%s, %s, '%s')" % (STCD, Z, TM)
        return self.__execute_insert(SQL)

    # 获取所有水位站点数据
    def get_all_station(self) -> list:
        SQL = "SELECT * FROM `station_code`"
        res_data = self.__execute_fetchall(SQL)
        return res_data
    
    # 获取某站点指定数量的水位数据
    def get_water_level(self, STCD: int, limit: int) -> list:
        SQL = "SELECT * FROM `water_level` where `STCD` = %s limit %s" % (STCD, limit)
        res_data = self.__execute_fetchall(SQL)
        return res_data
    
    def close(self) -> None:
        self.connection.close()
