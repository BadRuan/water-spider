from typing import List
from unittest import TestCase
from utils.logger import Logger
from model import StationConfig
from config.configuration import (
    getStations,
    getStationName,
    getDefaultDateRange,
    getInitDateRange,
)

logger = Logger(__name__)


class TestConfiguration(TestCase):

    def test_getStations(self):
        stations: List[StationConfig] = getStations()
        count: int = len(stations)
        logger.debug(f"配置文件有{count}条站点信息")

    def test_getStationName(self):
        stcd: int = 60115400
        name: str = "芜湖"
        _name: str = getStationName(stcd)
        self.assertEqual(name, _name)

        stcd: int = 62906500
        name: str = "清水"
        _name: str = getStationName(stcd)
        self.assertEqual(name, _name)
        logger.debug(f"测试站点代码查找站点名称")

    def test_getDateRange(self):
        default = getDefaultDateRange()
        init = getInitDateRange()
        logger.debug(f"测试获取配置文件日期范围")
