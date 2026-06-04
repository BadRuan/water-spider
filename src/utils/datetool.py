from datetime import datetime, timedelta
from typing import List, Optional, Final
from src.model import DateRange
from src.settings import DATE_SETTINGS


formatStr: Final[str] = "%Y%m%d%H%M"


def get_time_range(start_datetime_str: Optional[str], end_datetime_str: Optional[str]) -> List[DateRange]:
    """根据起止时间生成日期范围列表，自动按 cut_date_length 切割大范围"""
    now_time: datetime = datetime.now()

    if end_datetime_str is None:
        end_datetime = now_time
    else:
        end_datetime = datetime.strptime(end_datetime_str, formatStr)
        if end_datetime > now_time:
            end_datetime = now_time

    # 未指定开始时间，默认获取最近 N 天
    if start_datetime_str is None:
        start_datetime = end_datetime - timedelta(days=DATE_SETTINGS.latest_date_length)
        return [DateRange(
            start_time=start_datetime.strftime(formatStr),
            end_time=end_datetime.strftime(formatStr),
        )]

    start_datetime = datetime.strptime(start_datetime_str, formatStr)
    day_length: int = (end_datetime - start_datetime).days

    # 日期范围小于切割长度，不切割
    if day_length <= DATE_SETTINGS.cut_date_length:
        return [DateRange(
            start_time=start_datetime.strftime(formatStr),
            end_time=end_datetime.strftime(formatStr),
        )]

    # 按 cut_date_length 切割日期范围
    dates_list: List[DateRange] = []
    current_start = start_datetime
    while current_start < end_datetime:
        current_end = min(current_start + timedelta(days=DATE_SETTINGS.cut_date_length), end_datetime)
        dates_list.append(DateRange(
            start_time=current_start.strftime(formatStr),
            end_time=current_end.strftime(formatStr),
        ))
        current_start = current_end

    return dates_list
