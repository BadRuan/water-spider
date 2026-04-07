from datetime import datetime, timedelta
from typing import List, Optional
from src.model import DateRange
from src.settings import DATE_SETTINGS


formatStr = "%Y%m%d%H%M"

def get_time_range(start_datetime_str: Optional[str], end_datetime_str: Optional[str]) -> List[DateRange]:
    now_time: datetime = datetime.now()
    
    if end_datetime_str is None:
        end_datetime = now_time
    else:
        end_datetime = datetime.strptime(end_datetime_str, formatStr)
        # 防止结束时间超出当前时间
        if end_datetime > now_time:
            end_datetime = now_time
    if start_datetime_str is None: # 未给开始时间，按默认日期范围长度获取
        start_datetime = end_datetime - timedelta(days=DATE_SETTINGS.latest_date_length)
        return [DateRange(start_time=start_datetime.strftime(formatStr), end_time=end_datetime.strftime(formatStr))]
    else:
        start_datetime: datetime = datetime.strptime(start_datetime_str, formatStr)
        day_length: int = (end_datetime - start_datetime).days
        if day_length < DATE_SETTINGS.cut_date_length: # 日期范围小于日期切片长度，不切割
            return [DateRange(start_time=start_datetime.strftime(formatStr), end_time=end_datetime.strftime(formatStr))]
        else:
            count: int = day_length // DATE_SETTINGS.cut_date_length 
            dates_list: List[DateRange] = []
            dates_list.append(DateRange(start_time=start_datetime.strftime(formatStr), end_time=(start_datetime + timedelta(days=DATE_SETTINGS.cut_date_length)).strftime(formatStr)))
                
            for _ in range(count):
                start_datetime += timedelta(days=DATE_SETTINGS.cut_date_length)
                target_end_datetime: datetime = start_datetime + timedelta(days=DATE_SETTINGS.cut_date_length)
                if target_end_datetime > end_datetime:
                    target_end_datetime = end_datetime
                dates_list.append(DateRange(start_time=start_datetime.strftime(formatStr),end_time=target_end_datetime.strftime(formatStr)))
            return dates_list
        