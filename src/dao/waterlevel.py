from util.mysqltool import MySQLTool
from dao.abstract.waterlevel import WaterlevelAbstract


class WaterlevelDao(WaterlevelAbstract):
    def __init__(self) -> None:
        self.m = MySQLTool()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int:
        SQL = """CREATE TABLE IF NOT EXISTS `water_level` (
                    `ID` int(11) NOT NULL AUTO_INCREMENT,
                    `STCD` int(11) NOT NULL,
                    `Z` float(4, 2) NOT NULL,
                    `TM` datetime COLLATE utf8_bin NOT NULL ,
                    PRIMARY KEY (`ID`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;"""
        return await self.m.execute_sql(SQL)

    # 插入某条水位数据
    async def insert_water_level(self, STCD: int, Z: float, TM: str) -> int:
        SQL = f"INSERT INTO `water_level` (`STCD`, `Z`, `TM`) VALUES ({STCD}, {Z}, '{TM}')"
        return await self.m.execute_insert(SQL)

    # 获取某站点指定数量的水位数据
    async def get_water_level_list(self, STCD: int, limit: int) -> list:
        SQL = f"SELECT * FROM `water_level` where `STCD` = {STCD} limit {limit}"
        return await self.m.execute_fetchall(SQL)

    # 获取指定时间的水位数据
    async def get_water_level(self, STCD: int, TM: str) -> list:
        SQL = f"SELECT * FROM `water_level` where `STCD` = {STCD} and TM = '{TM}:00'"
        return await self.m.execute_fetchone(SQL)
