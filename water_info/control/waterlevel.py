import logging
from lib.datetool import get_date_list, getNowTM
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
    
    # 首次运行加载保存数据
    def first_load_waterlevel_datedata(self):
        logging.info("首次启动, 获取今年历史水位数据")
        for date_item in get_date_list():
            logging.info(f"获取时间{date_item}水位数据")
            self.save_waterlevel_info(date_item)
        logging.info("首次启动, 今年历史水位数据获取完成")

    def get_latest_data(self):
        now_date = getNowTM()
        logging.info(f"获取当前时间 {now_date} 水位数据")
        self.save_waterlevel_info(now_date)
        