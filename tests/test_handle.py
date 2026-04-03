from src.settings import STATIONS
from src.utils.logger import Logger
from src.model import RequestDateRange, Request
from src.handle import Handler, SendApiHandler, DecodeHandler


logger = Logger(__name__)

class TestHandler():
    def test_hanle(self):
        for station in STATIONS:
            request: Request = Request(station=station,date_range=RequestDateRange(start_time='202601010000',end_time='202601020000'))
            
            api_handle: Handler = SendApiHandler()
            decode_handle: Handler = DecodeHandler()
            
            api_handle.set_next(decode_handle)
            
            api_handle.handle(request)
            
            if len(request.data) == 0:
                logger.debug("解密数据为空")
            else:
                logger.debug(request)