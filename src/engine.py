from typing import List
from datetime import datetime
from time import sleep
from src.settings import STATIONS, DATE_SETTINGS
from src.utils.logger import Logger
from src.utils.datetool import get_time_range, formatStr
from src.model import RequestDateRange, Request
from src.handle import Handler, SendApiHandler, DecodeHandler


logger = Logger(__name__)

class Spider:
    
    def __init__(self) -> None:
        logger.info(DATE_SETTINGS)

    def _get_data(self, target_date: List[RequestDateRange]):
        for date_time in target_date:
            for station in STATIONS:
                request: Request = Request(station=station,date_range=date_time)
                api_handle: Handler = SendApiHandler() # 发送请求
                decode_handle: Handler = DecodeHandler() # 解析数据
                api_handle.set_next(decode_handle)
                api_handle.handle(request)
                sleep(1) # 休眠1秒
                logger.info(request)


    def run_in_24_hour(self):
        # while True:
        target_date: List[RequestDateRange] = get_time_range(end_datetime_str=None,start_datetime_str=None)
        self._get_data(target_date)
            

    def run_get_this_year_full_data(self):
        now: datetime = datetime.now()
        this_year_start: datetime = datetime(now.year, 1, 1)
        target_date: List[RequestDateRange] = get_time_range(end_datetime_str=now.strftime(formatStr),start_datetime_str=this_year_start.strftime(formatStr))
        self._get_data(target_date)
            
spider = Spider()