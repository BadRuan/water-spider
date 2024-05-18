import logging
from typing import List
from core.settings import STATIONS
from core.dao import ApiDao, WaterLevelData, insertWaterlevelToDdatabase


class ApiService:

    def __init__(self) -> None:
        self.dao = ApiDao()

    # 获取最新水位数据
    async def save_recently_data(self) -> None:
        for station in STATIONS:
            datas: List[WaterLevelData] = await self.dao.get_recently_data(station.stcd)
            count: int = await insert_waterlevels(datas)
            logging.info(f"获取{station.name}近期水位{len(datas)}条, 保存{count}条")

    # 初始化：获取指定年份所有水位数据
    async def save_target_year_datas(self, year: int) -> None:
        for station in STATIONS:
            datas: List[WaterLevelData] = await self.dao.get_target_year_datas(
                year, station.stcd
            )
            count: int = await insert_waterlevels(datas)
            logging.info(f"获取{year}年{station.name}水位{len(datas)}条, 保存{count}条")


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

        return count
