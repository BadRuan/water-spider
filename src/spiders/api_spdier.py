from spiders.base_spdier import SpierSubject
from utils.parser import Parser
from utils.water_security import WaterSecurity
from model import DataWaterlevel
from requests import post


class ApiSpider(SpierSubject):
    def __init__(self):
        super().__init__()
        self.tool = WaterSecurity()
        self.parser = Parser()
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

    def get_data(self) -> DataWaterlevel:
        playload = {
            "name": self.tool.encode("GetSwLineMap"),
            "stcd": "2.1MDYxMTQ1MDA=",
            "btime": "2.1MDI1MjIwNTA4MDAw",
            "etime": "2.1MDI1MjIwNTE2MTAw",
            "sttp": self.tool.encode("ZQ"),
            "waterEncode": self.tool.encode("true"),
        }
        r = post(url=self.url, headers=self.headers, data=playload, verify=False)
        data_waterlevel: DataWaterlevel = self.parser.translate(r.text)
        return data_waterlevel