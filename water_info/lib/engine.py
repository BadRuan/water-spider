import logging
from config.settings import STATIONS
from lib.requestData import RequestData
from lib.saveservice import SaveDateService

class Engine:
    def __init__(self) -> None:    
        pass

    def __loadTargetStation(self) -> bool:
        if len(STATIONS) == 0:
            return False
        else:
            c = len(STATIONS)
            logging.info(f"目标水文站{c}个, 准备获取数据")
            return True        

    def start(self, date: str):
        if self.__loadTargetStation():
            for s in STATIONS:
                logging.info(f"请求{s['NAME']}水文站数据")
                r = RequestData()
                data = r.getDecodeUsefulData(str(s['STCD']),date )
                service = SaveDateService(data)
                service.saveToDatabase()
                service.reprot()
            logging.info("数据获取并保存完毕")
        else:
            logging.error("目标水文站信息为空, 请添加")