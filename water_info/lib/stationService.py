import logging
from config.settings import STATIONS
from dao.database import MySQLTool

class StationService:
    def __init__(self) -> None:
        self.database = MySQLTool()

    def initStation(self):
        database = self.database
        for item in STATIONS:
            database.insert_station(item['STCD'], item['NAME'])
            logging.info(f"初始化{item['NAME']}站点信息")