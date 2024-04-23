import logging
from config.settings import STATIONS, DATE_RANGE_LENGTH
from dao.api import ApiDao


class ApiService:

    def __init__(self) -> None:
        self.dao = ApiDao()

    # 获取最新水位数据
    async def get_recently_data(self) -> list:
        data_dict = {}
        for station in STATIONS:
            datas = await self.dao.get_recently_data(station.stcd)
            data_dict[str(station.stcd)] = datas
            logging.info(f"获取到{station.name}近期水位数据: {len(datas)} 条.")
        return data_dict

    # 获取指定时间的水位数据
    async def get_target_data(
        self,
        input_datetime_str: str,
        days: int = DATE_RANGE_LENGTH.normal,
    ):
        data_dict = {}
        for station in STATIONS:
            datas = await self.dao.get_target_data(
                station.stcd, input_datetime_str, days
            )
            data_dict[str(station.stcd)] = datas
            logging.info(f"获取 {station.name} 水位数据: {len(datas)} 条.")
        return data_dict

    # 初始化：获取今年所有水位数据
    async def get_year_datas(self):
        data_dict = {}
        for station in STATIONS:
            datas = await self.dao.get_year_datas(station.stcd)
            data_dict[str(station.stcd)] = datas
            logging.info(f"获取到{station.name}今年水位数据: {len(datas)} 条.")
        return data_dict
