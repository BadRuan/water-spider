import logging
from json import loads
from util.requestData import RequestData
from util.datetool import getTM
from util.encodeTool import EncodeTool

class ApiService:
    def __init__(self) -> None:
        self.request = RequestData()
        self.tool = EncodeTool()

    def getResData(self, STCD: str, target_time: str) -> str:
        tool = self.tool
        date_range = getTM(target_time)
        # 请求参数加密
        data = {
            'name': tool.encrypt("GetSwLineMap"),
            'stcd': tool.encrypt(STCD),
            'btime': tool.encrypt(date_range['btime']),
            'etime': tool.encrypt(date_range['etime']),
            'sttp': tool.encrypt("ZQ"),
            'waterEncode': tool.encrypt("true")
        }
        logging.debug("请求参数: " , data)
        return self.request.getResData(data)

    def getDecodeData(self, STCD: str, target_time: str) -> str:
        data = self.getResData(STCD, target_time)
        encodeData = loads(data)['data']
        decodeData = self.tool.decrypt(encodeData)
        return decodeData