from time import sleep
from unittest import TestCase
from model import RequestDateRange
from utils.date_tool import DateTool
from utils.logger import Logger
from config.configuration import getStations
from spiders.api_spdier import ApiSpider


logger = Logger(__name__)


class TestSpider(TestCase):

    def test_get_data(self):
        datetool = DateTool()
        spider = ApiSpider()
        stcd1: int = 60115400  # 芜湖站
        stcd2: int = 62905100  # 新桥闸上
        request_daterange: RequestDateRange = datetool.get_recently_time_range()
        logger.debug(f"测试 芜湖[{stcd1}] 数据获取")
        spider.get_data(stcd1, request_daterange)
        sleep(3)
        logger.debug(f"测试 新桥闸上[{stcd2}] 数据获取")
        spider.get_data(stcd2, request_daterange)

    def test_get_all_station_recently_data(self):
        spider = ApiSpider()
        datetool = DateTool()
        request_daterange: RequestDateRange = datetool.get_recently_time_range()
        for station in getStations():
            logger.debug(f"测试 {station.name}[{station.stcd}] 数据获取")
            spider.get_data(station.stcd, request_daterange)
            sleep(3)
