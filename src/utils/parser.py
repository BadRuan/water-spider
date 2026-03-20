from json import loads
from typing import List
from model import WaterLevel
from utils.security import WaterSecurity
from utils.logger import Logger


logger = Logger(__name__)


class Parser:
    def __init__(self):
        self.tool = WaterSecurity()

    def translate(self, data: str) -> List[WaterLevel]:
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
        return [WaterLevel(height=i["Z"], tm=i["TM"]) for i in data_sw]
