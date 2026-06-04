from asyncio import sleep
from typing import List, AsyncGenerator
from datetime import datetime, timezone
from random import randint
from src.settings import stations
from src.utils import Logger, get_time_range, formatStr
from src.model import DateRange, Request
from src.handle import Handler, SendApiHandler, DecodeHandler, StorageHandle


log = Logger(__name__)


async def get_data(target_daterange: List[DateRange]) -> int:
    """获取指定日期范围内所有站点的水位数据，返回总条数"""
    total_count: int = 0
    for date_time in target_daterange:
        log.info("---------------------")
        log.info(f"开始获取时间 {date_time.start_time} => {date_time.end_time} 的数据")
        for station in stations:
            request = Request(code=station.code, name=station.name, date_range=date_time)

            # 构建责任链：发送请求 → 解析数据 → 存储数据
            api_handler = SendApiHandler()
            decode_handler = DecodeHandler()
            storage_handler = StorageHandle()
            api_handler.set_next(decode_handler).set_next(storage_handler)

            await api_handler.handle(request)
            count = len(request.data)
            total_count += count
            log.info(f"获取到 {request.name} {count} 条数据")
            await sleep(randint(1, 4))

        log.info(f"本轮共获取 {total_count} 条水位数据")
    return total_count


async def GenData() -> AsyncGenerator[int, None]:
    """无限生成器：持续获取最新数据"""
    while True:
        target_daterange = get_time_range(end_datetime_str=None, start_datetime_str=None)
        count = await get_data(target_daterange)
        yield count


class Spider:
    """水位爬虫调度器"""

    async def run_in_24_hour(self):
        """24 小时运行模式：随机间隔时间轮询"""
        gen = GenData()
        while True:
            await anext(gen)
            rand_seconds = randint(100, 600)
            log.info(f"{rand_seconds} 秒后开始下轮数据提取")
            await sleep(rand_seconds)

    async def get_this_year_full_data(self):
        """获取今年整年所有水位数据"""
        now = datetime.now(timezone.utc)
        year_start = datetime(now.year, 1, 1, tzinfo=timezone.utc)
        target_daterange = get_time_range(
            start_datetime_str=year_start.strftime(formatStr),
            end_datetime_str=now.strftime(formatStr),
        )
        await get_data(target_daterange)

    async def get_target_year_full_data(self, year: int):
        """获取指定年份整年所有水位数据"""
        year_start = datetime(year, 1, 1, tzinfo=timezone.utc)
        year_end = datetime(year, 12, 31, 23, 59, tzinfo=timezone.utc)
        target_daterange = get_time_range(
            start_datetime_str=year_start.strftime(formatStr),
            end_datetime_str=year_end.strftime(formatStr),
        )
        await get_data(target_daterange)

    async def get_target_daterange_range_data(self, start_time: str, end_time: str):
        """获取指定时间范围的水位数据"""
        target_daterange = get_time_range(start_time, end_time)
        await get_data(target_daterange)


spider = Spider()
