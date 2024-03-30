from requests import post
from json import loads
from lib.encodeTool import EncodeTool
from lib.datetool import getTM

class RequestData(object):

    def __init__(self) -> None:
        self.tool = EncodeTool()
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "DNT": "1",
            "Origin": "http://yc.wswj.net",
            "Referer": "http://yc.wswj.net/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        self.data = {
            "name": "",
            "stcd": "",
            "btime": "",
            "etime": "",
            "sttp": "",
            "waterEncode": "",
            "random": ""
        }
    
    def getResEncodeData(self, stcd: str, target_time: str) -> str:
        date_range = getTM(target_time)
        tool = self.tool
        # 请求参数加密
        self.data = {
            'name': tool.encrypt("GetSwLineMap"),
            'stcd': tool.encrypt(stcd),
            'btime': tool.encrypt(date_range['btime']),
            'etime': tool.encrypt(date_range['etime']),
            'sttp': tool.encrypt("ZQ"),
            'waterEncode': tool.encrypt("true")
        }
        # 必须发送加密请求
        response = post(url='http://61.191.22.196:5566/AHSXX/service/PublicBusinessHandler.ashx', headers=self.headers, data=self.data, verify=False)
        if response.status_code == 200:
            responseData = response.text
            return responseData
        elif response.status_code == 500: 
            raise ValueError("服务内部异常")
        else:
            raise ValueError("请求异常代码:", response.status_code)
    
    def getDecodeUsefulData(self, stcd: str, target_time: str) -> str:
        data = self.getResEncodeData(stcd, target_time)
        encodeData = loads(data)['data']
        decodeData = self.tool.decrypt(encodeData)
        return decodeData