import logging
from config.settings import STATIONS, DATE_RANGE_LENGTH
from service.abstract.api import ApiAbstract
from dao.api import ApiDao


class ApiService(ApiAbstract):

    def __init__(self) -> None:
        self.dao = ApiDao()

    # 获取最新水位数据
    async def get_recently_data(self) -> list:
        data = []
        for station in STATIONS:
            datas = await self.dao.get_recently_data(station["STCD"])
            for d in datas:
                data.append(d)
        logging.info(f"获取最新水位数据: {len(data)} 条.")
        return data

    # 获取指定时间的水位数据
    async def get_target_data(
        self,
        input_datetime_str: str,
        days: int = DATE_RANGE_LENGTH["normal"],
    ):
        data = []
        for station in STATIONS:
            datas = await self.dao.get_target_data(
                station["STCD"], input_datetime_str, days
            )
            for d in datas:
                data.append(d)
        logging.info(f"获取 {input_datetime_str} 时间水位数据: {len(data)} 条.")
        return data

    # 初始化：获取今年所有水位数据
    async def get_year_datas(self):
        data = []
        for station in STATIONS:
            datas = await self.dao.get_year_datas(
                station["STCD"]
            )
            for d in datas:
                data.append(d)
        logging.info(f"获取今年水位数据: {len(data)} 条.")
        return data
