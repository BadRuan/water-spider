import logging
from typing import List
from dao.waterlevel import WaterlevelDao
from dao.api import WaterLevelData

class WaterlevelService:

    def __init__(self) -> None:
        self.dao = WaterlevelDao()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int:
        result = await self.dao.create_waterlevel_table()
        if result:
            logging.info("创建水位数据表成功")
        else:
            logging.error("创建水位数据表失败")

    # 插入水位数据
    async def insert_water_level(self, waterlevels: List[WaterLevelData]) -> int:
        # 数据条目超过1000切片, 防止SQL语句过长
        def slice_list(data, length):
            return [data[i : i + length] for i in range(0, len(data), length)]

        length = len(waterlevels)
        if length == 0:
            logging.info("没有水位数据, 无需入库")
            return 0
        else:
            sliced_data = slice_list(waterlevels, 1000)
            count = 0
            for data in sliced_data:
                num = await self.dao.insert_water_level(data)
                count += num
            logging.info(f"共{length}条数据, 成功插入{count}条数据")
            return count
