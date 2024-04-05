import logging
from datetime import datetime, timedelta
from config.settings import DATE_RANGE_LENGTH

date_range = {
    "btime": '',
    "etime": ''
}

formatStr = "%Y%m%d%H%M"

def getNowTM() -> str:
    current = datetime.now()
    now_date_str = current.strftime(formatStr)
    date_range_length_ago = current - timedelta(days=DATE_RANGE_LENGTH)
    date_range['etime'] = now_date_str
    date_range['btime'] = date_range_length_ago.strftime(formatStr)
    logging.debug(f"最新请求时间范围, btime: {date_range['btime']}, etime: {date_range['etime']}.")
    return date_range

def getTM(input_datetime_str: str) -> str:
    # 日期格式: 202405011200
    if len(input_datetime_str) != 12:
        raise ValueError("时间长度不对, 参考这个: 202405010000")
    input_datetime = datetime.strptime(input_datetime_str, formatStr)
    if input_datetime > datetime.now():
        input_datetime = datetime.now()
    ten_days_ago = input_datetime - timedelta(days=DATE_RANGE_LENGTH)
    date_range['etime'] = input_datetime.strftime(formatStr)
    date_range['btime'] = ten_days_ago.strftime(formatStr)
    logging.debug(f"指定请求时间范围, btime: {date_range['btime']}, etime: {date_range['etime']}.")
    return date_range

def get_date_list() -> list:
    # 获取当年的第一天和当前日期
    this_year = datetime.now().year
    start_date = datetime(this_year, 1, 1)
    current_date = datetime.now()
    # 初始化日期列表和计数器
    dates_list = []
    count = 0
    # 循环生成每隔10天的日期直到达到或超过当前日期
    while start_date <= current_date:
        next_date = start_date + timedelta(days=DATE_RANGE_LENGTH * count)
        dates_list.append(next_date.strftime("%Y%m%d%H%M"))   
        # 检查下一个日期是否已经超过了当前日期
        if next_date > current_date:
            break
        count += 1
    return dates_list