from config.settings import STATIONS
from lib.requestData import RequestData
from lib.saveservice import SaveDateService

class Engine:
    def __init__(self) -> None:    
        pass

    def __loadTargetStation(self) -> None:
        if len(STATIONS) == 0:
            raise ValueError("没有目标水文站点数据信息")

    def start(self, date: str):
        self.__loadTargetStation()
        for s in STATIONS:
            print("获取 %s 水文站水位数据" % (s['NAME']))
            r = RequestData()
            data = r.getDecodeUsefulData(str(s['STCD']),date )
            service = SaveDateService(data)
            service.saveToDatabase()
            print(service.reprot())