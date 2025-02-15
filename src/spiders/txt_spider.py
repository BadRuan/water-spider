from spiders.base_spdier import SpierSubject
from utils.parser import Parser
from model import DataWaterlevel


# 从本地data.txt中读取数据，仅测试使用
class TxtSpider(SpierSubject):
    def __init__(self):
        super().__init__()
        self.parser = Parser()
        

    def get_data(self, *args, **kwargs) -> DataWaterlevel:
        with open("data.txt", "r", encoding="utf-8") as file:
            data_str: str = file.read()
            data_waterlevel: DataWaterlevel = self.parser.translate(data_str)
            return data_waterlevel
