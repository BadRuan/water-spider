import logging
from config.settings import STATIONS
from dao.station import StationDao

class StationService:
    def __init__(self) -> None:
        self.dao = StationDao()

    # 检查水文站表是否存在
    def check_table_exists(self) -> bool:
        if self.dao.check_table_exists():
            return True
        else:
            return False

    # 创建水文站表
    def create_station_table(self) -> int:
        return self.dao.create_station_table()

    # 初始化：插入现有水文站点信息
    def init_station(self):
        dao = self.dao
        for item in STATIONS:
            dao.insert_station(item['STCD'], item['NAME'])
            logging.info(f"初始化{item['NAME']}站点信息")