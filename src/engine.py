import logging
import time
from config.settings import REQUEST_INTRVAL
from control.station import StationControll
from control.waterlevel import WaterlevelControl
from control.threeline import ThreelineControl

logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)


class App:
    
    def __init__(self) -> None:
        self.station = StationControll()
        self.waterlevel = WaterlevelControl()
        self.threeline = ThreelineControl()

    # 首次启动初始化创建数据表
    def __first_start(self):
        if self.station.check_table_exists():
            logging.warning("数据表已存在, 无需初始化")     
        else:
            logging.info("数据库为空, 即将执行初始化操作")
            # 初始化创建数据表
            self.station.init_station()
            self.waterlevel.init_threeline()
            self.threeline.init_threeline()
            # 首次加载数据
            self.waterlevel.first_load_waterlevel_datedata()
    
    # 正常启动项目采集水位信息功能，需要指定时间
    def start(self):
        self.__first_start()
        while True:
            self.waterlevel.get_latest_data()
            time.sleep(REQUEST_INTRVAL * 60)

