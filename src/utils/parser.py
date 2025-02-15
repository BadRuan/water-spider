from json import loads, JSONDecodeError
from typing import List
from model import WaterLevel, DataWaterlevel
from config.settings import MODE
from config.configuration import Configuration
from utils.water_security import WaterSecurity
from utils.logger import Logger


logger = Logger(__name__)


class Parser:
    def __init__(self):
        super().__init__()
        self.config = Configuration(MODE)
        self.tool = WaterSecurity()

    def _getStationName(self, stcd: int) -> str:
        stations = self.config.getStations()
        for station in stations:
            if stcd == station["stcd"]:
                return station["name"]
            
        _msg = f"配置文件无此站点{stcd} 信息"
        logger.error(_msg)
        raise ValueError(_msg)

    def translate(self, data: str) -> DataWaterlevel:
        try:
            _r = loads(data)
            
            # 通过响应码 respCode 判断响应是否成功
            respCode: str = _r["respCode"]
            if "0" != respCode:
                _msg: str = f"响应错误，错误信息为 {_r['respMsg']}"
                logger.error(_msg)
                raise ValueError(_msg)

            encode_str: str = _r["data"]  # 从响应内容取出加密数据内容
            decode_str: str = self.tool.decode(encode_str)
            json_obj = loads(decode_str)
            data_sw: List = json_obj["data_sw"]

            count: int = len(data_sw)
            if 0 == count:
                _msg: str = "返回0条水位数据"
                logger.error(_msg)
                raise ValueError(_msg)
            
            waterlevels: List[WaterLevel] = []

            for i in data_sw:
                waterlevels.append(WaterLevel(z=i["Z"], tm=i["TM"]))
            stcd: int = int(data_sw[0]["STCD"])
            name = self._getStationName(stcd)
            data_waterlevel: DataWaterlevel = DataWaterlevel(
                name=name, stcd=stcd, count=count, data=waterlevels
            )
            
            logger.info(f"解析 {name}站[{stcd}]:{count}条水位数据")
            return data_waterlevel
        except JSONDecodeError:
            logger.error("JSON解析异常")
