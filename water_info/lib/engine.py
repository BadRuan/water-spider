import logging
from config.settings import STATIONS
from lib.requestData import RequestData
from lib.saveservice import SaveDateService

class Engine:
    def __init__(self) -> None:    
        pass

    def __loadTargetStation(self) -> bool:
        if len(STATIONS) == 0:
            logging.error("目标水文站信息为空, 请添加")
            return False
        else:
            return True        

    def start(self, date: str):
        if self.__loadTargetStation():
            for s in STATIONS:
                logging.info(f"开始请求 {s['NAME']} 水文站水位数据")
                r = RequestData()
                data = r.getDecodeUsefulData(str(s['STCD']),date )
                service = SaveDateService(data)
                service.saveToDatabase()
                service.reprot()