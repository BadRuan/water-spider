from dao.mysqltool import MySQLTool

class WaterlevelDao:
    def __init__(self) -> None:
        self.m = MySQLTool()

    # 插入某条水位数据
    def insert_water_level(self, STCD: int, Z: float, TM: str) -> int:
        SQL = "INSERT INTO `water_level` (`STCD`, `Z`, `TM`) VALUES (%s, %s, '%s')" % (STCD, Z, TM)
        return self.m.execute_insert(SQL)
    
    # 获取某站点指定数量的水位数据
    def get_water_level_list(self, STCD: int, limit: int) -> list:
        SQL = "SELECT * FROM `water_level` where `STCD` = %s limit %s" % (STCD, limit)
        res_data = self.m.execute_fetchall(SQL)
        return res_data

    # 获取指定时间的水位数据
    def get_water_level(self, STCD: int, TM: str):
        SQL = "SELECT * FROM `water_level` where `STCD` = %s and TM = '%s:00'" % (STCD, TM)
        res_data = self.m.execute_fetchone(SQL)
        return res_data
    
    # 关闭数据库连接
    def close(self):
        self.dao.close()