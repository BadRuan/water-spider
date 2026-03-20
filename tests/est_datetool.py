from typing import List
from src.utils.datetool import DateTool
from src.utils.logger import Logger
from src.model import RequestDateRange


logger = Logger(__name__)

class TestDateTool():
    def test_get_time_range(self):
        datetool = DateTool()
        test_str: str = '202604121222'
        r_list: List[RequestDateRange] = datetool.get_time_range(end_datetime_str=test_str,start_datetime_str=None)
        logger.debug(f"1. Test get latest date range {test_str}")
        for i in r_list:
            logger.debug(f"date range: {i.start_time} -> {i.end_time}")
        
        test_str: str = '202604121222'
        r_list: List[RequestDateRange] = datetool.get_time_range(end_datetime_str=test_str,start_datetime_str='202601011222')
        logger.debug(f"2. Test get long date range {test_str}")
        for i in r_list:
            logger.debug(f"date range: {i.start_time} -> {i.end_time}")
