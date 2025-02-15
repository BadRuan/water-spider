from requests import post
from typing import List
from time import sleep
from utils.parser import Parser
from utils.water_security import WaterSecurity
from utils.date_tool import DateTool
from utils.logger import Logger
from config.configuration import Configuration
from model import DataWaterlevel, RequestDateRange
from spiders.base_spdier import SpierSubject


logger = Logger(__name__)


class ApiSpider(SpierSubject):
    def __init__(self):
        super().__init__()
        self.water_security = WaterSecurity()
        self.parser = Parser()
        self.datetool = DateTool()
        self.config = Configuration()
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "DNT": "1",
            "Origin": "http://yc.wswj.net",
            "Referer": "http://yc.wswj.net/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        }
        self.url = "http://61.191.22.196:5566/AHSXX/service/PublicBusinessHandler.ashx"

    def get_data(self, stcd: int, date_range: RequestDateRange) -> DataWaterlevel:
        playload = {
            "name": self.water_security.encode("GetSwLineMap"),
            "stcd": self.water_security.encode(str(stcd)),
            "btime": self.water_security.encode(date_range.btime),
            "etime": self.water_security.encode(date_range.etime),
            "sttp": self.water_security.encode("ZQ"),
            "waterEncode": self.water_security.encode("true"),
        }
        r = post(url=self.url, headers=self.headers, data=playload, verify=False)
        if 200 != r.status_code:
            _msg: str = f"网络异常或服务器未响应，状态码为: {r.status_code}"
            logger.error(_msg)
            raise ValueError(_msg)
        sleep(2)
        data_waterlevel: DataWaterlevel = self.parser.translate(r.text)
        return data_waterlevel

    def get_recently_data(self) -> List[DataWaterlevel]:
        date_range: RequestDateRange = self.datetool.get_recently_time_range()
        stations: List = self.config.getStations()
        return [self.get_data(station, date_range) for station in stations[0]]
