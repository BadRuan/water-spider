import logging
from json import loads
from util.apiData import ApiData
from util.datetool import getTM
from util.encodeTool import EncodeTool

class ApiService:
    def __init__(self) -> None:
        self.api = ApiData()
        self.tool = EncodeTool()

    # 获取响应数据
    async def getResData(self, STCD: str, target_time: str) -> str:
        tool = self.tool
        date_range = getTM(target_time)
        data = {
            'name': tool.encrypt("GetSwLineMap"),
            'stcd': tool.encrypt(STCD),
            'btime': tool.encrypt(date_range['btime']),
            'etime': tool.encrypt(date_range['etime']),
            'sttp': tool.encrypt("ZQ"),
            'waterEncode': tool.encrypt("true")
        }
        logging.debug("请求参数: " , data)
        return await self.api.getResData(data)

    # 获取解密数据
    async def getDecodeData(self, STCD: str, target_time: str) -> str:
        data = await self.getResData(STCD, target_time)
        encodeData = loads(data)['data']
        decodeData = self.tool.decrypt(encodeData)
        return decodeData
    