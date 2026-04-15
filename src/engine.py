from typing import List
from datetime import datetime
from time import sleep
from random import randint
from settings import STATIONS 
from utils import Logger, get_time_range, formatStr, recoder_count_change
from model import DateRange, Request
from handle import Handler, SendApiHandler, DecodeHandler, StorageHandle


log = Logger(__name__)

class Spider:

    @recoder_count_change
    def _get_data(self, target_date: List[DateRange]):
        for date_time in target_date:
            log.info("---------------------")
            log.info(f"开始获取时间 {date_time.start_time} => {date_time.end_time} 的数据")
            count: int = 0
            for station in STATIONS:
                request: Request = Request(code=station.code, name=station.name,date_range=date_time)
                api_handle: Handler = SendApiHandler() # 发送请求
                decode_handle: Handler = DecodeHandler() # 解析数据
                storage_handle: Handler = StorageHandle() # 存储数据
                api_handle.set_next(decode_handle)
                decode_handle.set_next(storage_handle)
                
                api_handle.handle(request)
                _count: int = len(request.data)
                count += _count
                log.info(f"成功获取{request.name} {_count} 条数据")
                sleep(2.5)
            log.info(f"本轮共同获取 {count} 条水位数据")

    def run_in_24_hour(self):
        while True:
            target_date: List[DateRange] = get_time_range(end_datetime_str=None,start_datetime_str=None)
            self._get_data(target_date)
            rand_number: int = randint(100, 600)
            log.info(f"休息 {rand_number} 秒继续")
            sleep(rand_number)

    def get_this_year_full_data(self):
        now: datetime = datetime.now()
        this_year_start: datetime = datetime(now.year, 1, 1)
        target_date: List[DateRange] = get_time_range(end_datetime_str=now.strftime(formatStr),start_datetime_str=this_year_start.strftime(formatStr))
        self._get_data(target_date)
    
    def get_target_year_full_data(self, year: int):
        year_start: datetime = datetime(year, 1, 1)
        year_end: datetime = datetime(year, 12, 31)
        target_date: List[DateRange] = get_time_range(end_datetime_str=year_end.strftime(formatStr),start_datetime_str=year_start.strftime(formatStr))
        self._get_data(target_date)

    def get_target_date_range_data(self, start_time: str, end_time: str):
        target_date: List[DateRange] = get_time_range(start_time, end_time)
        self._get_data(target_date)

           
spider = Spider()
