import logging
from config.settings import STATIONS
from dao.station import StationDao

class StationService:
    def __init__(self) -> None:
        self.dao = StationDao()

    # 初始化：插入现有水文站点信息
    def initStation(self):
        dao = self.dao
        for item in STATIONS:
            dao.insert_station(item['STCD'], item['NAME'])
            logging.info(f"初始化{item['NAME']}站点信息")