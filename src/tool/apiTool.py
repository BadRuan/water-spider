from requests import get
from json import loads
from tool.dataTool import DataTool

ModuleidType = {
    'GetLyOrProviceSQBriefing' : '56',
    'GetDXSKSQBriefing' : '59'
}
    

class ApiTool:

    def __init__(self) -> None:
        self.tool = DataTool()
        self.data = ''
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Dnt': '1',
            'Host': '61.191.22.196:5566',
            'Origin': 'http://yc.wswj.net',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://yc.wswj.net/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        self.params = {
            'name': '',
            'moduleid': '',
            'time': '',
            'waterEncode': ''
        }
    
    def getData(self, name: str, time: str) -> str:
        tool = self.tool
        # 请求参数加密
        self.params = {
            'name': tool.encrypt(name),
            'moduleid': tool.encrypt(ModuleidType[name]),
            'time': tool.encrypt(time),
            'waterEncode': tool.encrypt('true')
        }
        # 必须发送加密请求
        response = get(url='http://61.191.22.196:5566/ahsxx/service/BriefHandler.ashx', params=self.params, headers=self.headers)
        if response.status_code == 200:
            responseData = response.text
            encodeData = loads(responseData)['data']
            decodeData = self.tool.decrypt(encodeData)
            return decodeData
        elif response.status_code == 500: 
            raise ValueError("服务内部异常")
        else:
            raise ValueError("请求异常:", response.status_code)
    
