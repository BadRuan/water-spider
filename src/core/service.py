import logging
from typing import List
from core.settings import STATIONS, DATE_RANGE_LENGTH
from core.dao import ApiDao, WaterLevelData, insertWaterlevelToDdatabase


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

    # 初始化：获取指定年份所有水位数据
    async def get_target_year_datas(self, year: int):
        data_dict = {}
        for station in STATIONS:
            datas = await self.dao.get_target_year_datas(year, station.stcd)
            data_dict[str(station.stcd)] = datas
            logging.info(f"获取到{year}年 {station.name} 水位数据: {len(datas)} 条.")
        return data_dict


# 插入水位数据
async def insert_waterlevels(waterlevels: List[WaterLevelData]) -> int:

    length = len(waterlevels)
    if length == 0:
        logging.info("无水位数据")
        return 0
    else:
        # 数据条目超过1000切片, 防止SQL语句过长
        def slice_list(data, length):
            return [data[i : i + length] for i in range(0, len(data), length)]

        sliced_data = slice_list(waterlevels, 1000)
        count = 0
        for data in sliced_data:
            num = await insertWaterlevelToDdatabase(data)
            count += num
        logging.info(f"共{length}条数据, 成功插入{count}条数据")
        return count
