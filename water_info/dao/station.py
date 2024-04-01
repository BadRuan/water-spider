from dao.mysqltool import MySQLTool

class StationDao:
    def __init__(self) -> None:
        self.dao = MySQLTool()

    # 插入水位站点代码
    def insert_station(self, STCD: int, NAME: str) -> int:
        SQL = "INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (%s, '%s')" % (STCD, NAME)
        return self.dao.execute_insert(SQL)
    
    # 获取所有水位站点数据
    def get_all_station(self) -> list:
        SQL = "SELECT * FROM `station_code`"
        res_data = self.dao.execute_fetchall(SQL)
        return res_data
    
    # 关闭数据库连接
    def close(self):
        self.dao.close()