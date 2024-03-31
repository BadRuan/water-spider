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
    five_days_ago = current - timedelta(days=5)
    date_range['etime'] = now_date_str
    date_range['btime'] = five_days_ago.strftime(formatStr)
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
