import logging
from config.settings import STATIONS
from service.abstract.station import StationAbstract
from dao.station import StationDao


class StationService(StationAbstract):
    def __init__(self) -> None:
        self.dao = StationDao()

    # 检查水文站表是否存在
    async def check_table_exists(self) -> bool:
        if await self.dao.check_table_exists():
            return True
        else:
            return False

    # 创建水文站表
    async def create_station_table(self) -> int:
        return await self.dao.create_station_table()

    # 初始化：插入现有水文站点信息
    async def init_station(self):
        for item in STATIONS:
            await self.dao.insert_station(item["STCD"], item["NAME"])
            logging.info(f"初始化{item['NAME']}站点信息")
