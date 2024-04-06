from dao.mysqltool import MySQLTool
from dao.abstract.waterlevel import WaterlevelAbstract

class WaterlevelDao(WaterlevelAbstract):
    def __init__(self) -> None:
        self.m = MySQLTool()

    # 创建水位数据表
    def create_waterlevel_table(self) -> int:
        SQL = """CREATE TABLE IF NOT EXISTS `water_level` (
                    `ID` int(11) NOT NULL AUTO_INCREMENT,
                    `STCD` int(11) NOT NULL,
                    `Z` float(4, 2) NOT NULL,
                    `TM` datetime COLLATE utf8_bin NOT NULL ,
                    PRIMARY KEY (`ID`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;"""
        return self.m.execute(SQL)

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