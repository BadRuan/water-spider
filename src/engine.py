from time import sleep
from typing import List
from model import DataWaterlevel, RequestDateRange
from utils.date_tool import DateTool
from utils.logger import Logger
from config.configuration import getStations
from spiders.api_spdier import ApiSpider
from storages.database_storage import DatabaseStorage


logger = Logger(__name__)


class Engine:
    def __init__(self):
        self.datetool = DateTool()
        self.spider = ApiSpider()

    def run(self):
        logger.info(f"开始爬虫任务")
        with DatabaseStorage() as storage:
            for station in getStations():
                logger.info(f"获取{station.name}[{station.stcd}]水位数据")
                dataWaterlevel: DataWaterlevel = self.spider.get_data(
                    station.stcd, self.datetool.get_recently_time_range()
                )
                storage.insert_waterlevel(dataWaterlevel)
                logger.info(f"{station.name}[{station.stcd}]水位数据已保存")
                logger.info(f"等待11秒, 执行后续任务")
                sleep(5)
        logger.info(f"爬虫运行结束")

    def init(self, year: int = 2025):
        logger.info(f"开始爬虫任务")
        logger.info(f"获取{year}年全年水位数据")
        with DatabaseStorage() as storage:
            for station in getStations():
                logger.info(f"获取{station.name}[{station.stcd}] {year}年 水位数据")
                for daterange_item in self.datetool.get_target_year_date_range_list(
                    year
                ):
                    dataWaterlevel: DataWaterlevel = self.spider.get_data(
                        station.stcd, daterange_item
                    )
                    storage.insert_waterlevel(dataWaterlevel)
                    logger.info(f"{station.name}[{station.stcd}]水位数据已保存")
                    logger.info(f"等待5秒, 执行后续任务")
                    sleep(5)
        logger.info(f"爬虫运行结束")
