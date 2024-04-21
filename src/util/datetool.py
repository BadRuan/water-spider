from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import List
from config.settings import DATE_RANGE_LENGTH

formatStr = "%Y%m%d%H%M"  # 时间示例: 202401041200


class DateRange(BaseModel):
    btime: str
    etime: str


# 输入结束时间，生成指定范围长度的时间范围
def get_time_range(
    input_datetime_str: str, day_length: int = DATE_RANGE_LENGTH["normal"]
) -> DateRange:
    # 日期格式: 202405011200
    if len(input_datetime_str) != 12:
        raise ValueError("时间长度不对, 参考这个: 202405010000")
    input_datetime = datetime.strptime(input_datetime_str, formatStr)
    if input_datetime > datetime.now():
        input_datetime = datetime.now()
    # 确定开始时间
    days_ago = input_datetime - timedelta(days=day_length)
    return DateRange(
        btime=days_ago.strftime(formatStr), etime=input_datetime.strftime(formatStr)
    )


# 获取最近时间范围
def get_recently_time_range() -> DateRange:
    now_time: str = datetime.now().strftime(formatStr)
    return get_time_range(now_time)


# 获取初始化日期列表
def get_init_date_list(day: int = DATE_RANGE_LENGTH["init"]) -> List[DateRange]:
    # 获取当年的第一天
    this_year = datetime.now().year
    start_date = datetime(this_year, 1, 1)
    # 获取当前日期
    current_date = datetime.now()
    # 初始化日期列表和计数器
    dates_list = []
    count = 0
    # 循环生成每隔day天的日期直到达到或超过当前日期
    while start_date <= current_date:
        next_date = start_date + timedelta(days=day * count)
        dates_list.append(next_date.strftime("%Y%m%d%H%M"))
        # 检查下一个日期是否已经超过了当前日期
        if next_date > current_date:
            break
        count += 1
    return dates_list


# 获取初始化日期范围列表
def get_init_data_range_list(day: int = DATE_RANGE_LENGTH["init"]) -> List[DateRange]:
    return [get_time_range(init_day, day) for init_day in get_init_date_list(day)]
