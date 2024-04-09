from util.mysqltool import MySQLTool
from dao.abstract.station import StationAbstract

class StationDao(StationAbstract):
    def __init__(self) -> None:
        self.dao = MySQLTool()

    # 创建水文站表
    async def create_station_table(self) -> int:
        SQL = """CREATE TABLE IF NOT EXISTS `station_code` (
                `ID` int(11) NOT NULL AUTO_INCREMENT,
                `STCD` int(11) NOT NULL UNIQUE,
                `NAME` varchar(255) COLLATE utf8_bin NOT NULL,
                PRIMARY KEY (`ID`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;"""
        return self.dao.execute(SQL)

    # 检查水文站表是否存在
    async def check_table_exists(self) -> int:
        SQL = f"SHOW TABLES LIKE '%station_code%'"
        return await self.dao.execute_sql(SQL)

    # 插入水位站点代码
    async def insert_station(self, STCD: int, NAME: str) -> int:
        SQL = "INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (%s, '%s')" % (STCD, NAME)
        return await self.dao.execute_insert(SQL)
    
    # 获取所有水位站点数据
    async def get_all_station(self) -> list:
        SQL = "SELECT * FROM `station_code`"
        return await self.dao.execute_fetchall(SQL)