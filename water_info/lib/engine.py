import logging
from config.settings import STATIONS
from lib.requestData import RequestData
from service.waterlevel import WaterlevelService
from service.station import StationService
from service.threeline import ThreeLineService

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
                service = WaterlevelService(data)
                service.saveToDatabase()
                service.reprot()
            logging.info("数据获取并保存完毕")
        else:
            logging.error("目标水文站信息为空, 请添加")
    
    def init_station(self):
        s = StationService()
        s.initStation()
    
    def init_three(self):
        s = ThreeLineService()
        s.init_three_line()

    def get_all_three_line(self):
        s = ThreeLineService()
        for i in s.get_all_three_line_list():
            logging.info(i)