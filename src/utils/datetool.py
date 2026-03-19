from datetime import datetime, timedelta
from typing import List, Optional
from model import RequestDateRange
from utils.logger import Logger
from config.settings import Default_Date_Range, Init_Date_Range



logger = Logger(__name__)
formatStr = "%Y%m%d%H%M"


class DateTool:
    def __init__(self):
        self.normal: int = Default_Date_Range
        self.init: int = Init_Date_Range

    def get_time_range(
        self, input_datetime_str: str, day_length: int
    ) -> Optional[RequestDateRange]:
        try:
            # 验证输入时间长度
            if len(input_datetime_str) != 12:
                message = "时间长度错误"
                logger.error(message)
                raise ValueError(message)
            # 验证时间是否晚于当前时间
            input_datetime = datetime.strptime(input_datetime_str, formatStr)
            if input_datetime > datetime.now():
                message = f"输入时间 {input_datetime_str} 晚于当前时间"
                logger.error(message)
                raise ValueError(message)
            # 确定开始时间
            days_ago = input_datetime - timedelta(days=day_length)
            return RequestDateRange(
                start_time=days_ago.strftime(formatStr),
                end_time=input_datetime.strftime(formatStr),
            )
        except Exception as error:
            logger.error(error)

    # 获取最近时间范围
    def get_recently_time_range(self) -> Optional[RequestDateRange]:
        now_time: str = datetime.now().strftime(formatStr)
        return self.get_time_range(now_time, self.normal)

    def _get_target_year_date_list(self, year: int) -> List[str]:
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        # 获取当前日期
        current_date = datetime.now()
        if start_date > current_date:
            message = "指定年份不能晚于当前年份"
            logger.error(message)
            raise ValueError(message)
        if end_date > current_date:
            logger.warning("指定年份为今年，更新截止时间为当前时间")
            end_date = current_date
        # 初始化日期列表和计数器
        dates_list = []
        count = 0
        # 循环生成每隔day天的日期直到达到或超过当前日期
        while start_date <= end_date:
            next_date = start_date + timedelta(days=self.init * count)
            dates_list.append(next_date.strftime(formatStr))
            # 检查下一个日期是否已经超过了当前日期
            if next_date > end_date:
                break
            count += 1
        del dates_list[0] # 删除上年末日期
        return dates_list

    # 获取指定年份的日期列表
    def get_target_year_date_range_list(self, year: int) -> List[Optional[RequestDateRange]]:
        return [
            self.get_time_range(init_day, self.init)
            for init_day in self._get_target_year_date_list(year)
        ]
        