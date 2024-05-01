import logging
from typing import List
from dao.waterlevel import insert_water_level
from dao.api import WaterLevelData


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
            num = await insert_water_level(data)
            count += num
        logging.info(f"共{length}条数据, 成功插入{count}条数据")
        return count
