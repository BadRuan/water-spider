from datetime import datetime, timedelta
from typing import List
from model import RequestDateRange
from utils.logger import Logger
from config.configuration import getDefaultDateRange, getInitDateRange


logger = Logger(__name__)
formatStr = "%Y%m%d%H%M"


class DateTool:
    def __init__(self):
        self.normal: int = getDefaultDateRange()
        self.init: int = getInitDateRange()

    def get_time_range(
        self, input_datetime_str: str, day_length: int
    ) -> RequestDateRange:
        try:
            if len(input_datetime_str) != 12:
                raise ValueError("输入时间长度错误")
            # 将输入时间由字符串转化为python标准格式的时间
            input_datetime = datetime.strptime(input_datetime_str, formatStr)
            # 防止大于当前时间
            if input_datetime > datetime.now():
                logger.warning(f"输入时间 {input_datetime_str} 晚于当前时间")
                input_datetime = datetime.now()
            # 确定开始时间
            days_ago = input_datetime - timedelta(days=day_length)
            return RequestDateRange(
                btime=days_ago.strftime(formatStr),
                etime=input_datetime.strftime(formatStr),
            )
        except Exception as error:
            logger.error(error)

    # 获取最近时间范围
    def get_recently_time_range(self) -> RequestDateRange:
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
    def get_target_year_date_range_list(self, year: int) -> List[RequestDateRange]:
        return [
            self.get_time_range(init_day, self.init)
            for init_day in self._get_target_year_date_list(year)
        ]
        