import logging
from config.settings import STATIONS
from service.api import ApiService
from service.waterlevel import WaterlevelService

class WaterlevelControl:
    def __init__(self) -> None:
        self.s = WaterlevelService()

    # 初始化水位信息表
    def init_threeline(self):
        flag = self.s.create_waterlevel_table()
        if flag:
            logging.info("成功创建水位信息表")
        else:
            logging.info("水位信息表创建失败")
    
    # 确认配置文件中目标水文站点信息
    def __loadTargetStation(self) -> bool:
        if len(STATIONS) == 0:
            return False
        else:
            c = len(STATIONS)
            logging.info(f"目标水文站{c}个, 准备获取水位数据")
            return True    

    # 保存水位信息到数据库中
    def save_waterlevel_info(self, date: str):
        if self.__loadTargetStation():
            for s in STATIONS:
                logging.info(f"请求{s['NAME']}水文站数据")
                r = ApiService()
                data = r.getDecodeData(str(s['STCD']),date )
                self.s.load_data(data)
                self.s.saveToDatabase()
                self.s.reprot()
            logging.info("数据获取并保存完毕")
        else:
            logging.error("目标水文站信息为空, 请添加")