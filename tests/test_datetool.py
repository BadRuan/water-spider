from typing import List
from src.utils.datetool import get_time_range
from src.utils.logger import Logger
from src.model import RequestDateRange


logger = Logger(__name__)


def test_get_time_range():
    test_str: str = '202604121222'
    r_list: List[RequestDateRange] = get_time_range(end_datetime_str=test_str,start_datetime_str=None)
    logger.debug(f"1. 测试获取最近的时间范围 202604121222")
    for i in r_list:
        logger.debug(f"date range: {i.start_time} -> {i.end_time}")
    
    test_str: str = '202604121222'
    r_list: List[RequestDateRange] = get_time_range(end_datetime_str=test_str,start_datetime_str='202601011222')
    logger.debug(f"2. 测试获取长的时间范围 {test_str}")
    for i in r_list:
        logger.debug(f"date range: {i.start_time} -> {i.end_time}")
    
    r_list: List[RequestDateRange] = get_time_range(end_datetime_str=None,start_datetime_str=None)
    logger.debug(f"3. 测试获取最近的时间范围")
    for i in r_list:
        logger.debug(f"date range: {i.start_time} -> {i.end_time}")