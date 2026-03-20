from abc import ABC, abstractmethod
from typing import Optional
from requests import post
from model import Request
from utils.logger import Logger
from utils.parser import Parser
from utils.security import WaterSecurity


logger = Logger(__name__)


class Handler(ABC):
    def __init__(self, successor: Optional['Handler'] = None):
        self._successor = successor

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._successor = handler
        return handler

    @abstractmethod
    def handle(self, request: Request) -> Optional[str]:
        if self._successor:
            return self._successor.handle(request)
        return None

class SendApiHandler(Handler):
    def __init__(self, successor: Handler | None = None):
        super().__init__(successor)
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "DNT": "1",
            "Origin": "http://yc.wswj.net",
            "Referer": "http://yc.wswj.net/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        }
        self.url = "http://61.191.22.196:5566/AHSXX/service/PublicBusinessHandler.ashx"
    
    def handle(self, request: Request) -> str | None:
        water_security = WaterSecurity()
        playload = {
            "name": water_security.encode("GetSwLineMap"),
            "stcd": water_security.encode(str(request.code)),
            "btime": water_security.encode(request.date_range.start_time),
            "etime": water_security.encode(request.date_range.end_time),
            "sttp": water_security.encode("ZQ"),
            "waterEncode": water_security.encode("true"),
        }
        # 解决新桥闸上参数不一致问题
        if request.code == 62905100:
            playload["name"] = water_security.encode("GetSwLineAndZX")
            playload["sttp"] = water_security.encode("DD")
            playload["zxstcd"] = water_security.encode("62905200")
            playload["zxsttp"] = water_security.encode("ZZ")
        
        r = post(url=self.url, headers=self.headers, data=playload, verify=False)
        if 200 != r.status_code:
            _msg: str = f"网络异常或服务器未响应，状态码为: {r.status_code}"
            logger.error(_msg)
            raise ValueError(_msg)
        request.encode_date =  r.text
        if self._successor:
            self._successor.handle(request)
            
class DecodeHandler(Handler):
    def handle(self, request: Request) -> str | None:
        if request.encode_date is not None:
            parser = Parser()
            request.data = parser.translate(request.encode_date)
        if self._successor:
            self._successor.handle(request)
            
class ChoiceHandler(Handler):
    def handle(self, request: Request) -> str | None:
        count: int = len(request.data)
        if count > 100:
            logger.debug("摘除前100条数据")
            request.data = request.data[100:]
        if self._successor:
            self._successor.handle(request)