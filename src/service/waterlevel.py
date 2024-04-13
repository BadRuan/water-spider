import logging
from config.settings import STATIONS2
from dao.waterlevel import WaterlevelDao


class WaterlevelService:

    def __init__(self) -> None:
        self.dao = WaterlevelDao()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int: 
        result =  await self.dao.create_waterlevel_table()
        if result:
            logging.info("创建水位数据表成功")
        else:
            logging.error("创建水位数据表失败")


    # 插入水位数据
    async def insert_water_level(self, waterlevels: list) -> int:
        if len(waterlevels) == 0:
            logging.error("没有水位数据, 无需入库")
        else:
            NAME = STATIONS2[waterlevels[0]["STCD"]]
            num = await self.dao.insert_water_level(waterlevels)
            logging.info(f"{NAME}水文站数据入库情况: 成功 {num} 条 / 总 {len(waterlevels)} 条.")
            
