import logging
from requests import post

class RequestData(object):

    def __init__(self) -> None:  
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
    
    def getResData(self, request_data) -> str:
        # 必须发送加密请求
        response = post(url='http://61.191.22.196:5566/AHSXX/service/PublicBusinessHandler.ashx', 
                        headers=self.headers, 
                        data=request_data, 
                        verify=False)
        if response.status_code == 200:
            responseData = response.text
            return responseData
        else:
            logging.error(f"水文数据库服务器响应错误, 错误码: {response.status_code}")
            raise ValueError("请求异常代码:", response.status_code)