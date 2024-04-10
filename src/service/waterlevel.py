import logging
from service.abstract.waterlevel import WaterlevelAbstract
from dao.waterlevel import WaterlevelDao


class WaterlevelService(WaterlevelAbstract):

    def __init__(self) -> None:
        self.dao = WaterlevelDao()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int:
        return await self.dao.create_waterlevel_table()

    # 检查数据库中对应水位站的水位数据是否存在
    async def __checkDataExists(self, STCD: int, TM: str) -> bool:
        data = await self.dao.get_water_level(
            STCD, TM
        )  # 从数据库查询这个 时间 水位 数据是否存在
        if data:
            return True
        else:
            return False

    # 插入某条水位数据
    async def insert_water_level(self, STCD: int, Z: float, TM: str) -> int:
        return await self.dao.insert_water_level(STCD, Z, TM)

    # 获取某站点指定数量的水位数据
    async def get_water_level_list(self, STCD: int, limit: int) -> list:
        return await self.dao.get_water_level_list(STCD, limit)

    # 获取指定时间的水位数据
    async def get_water_level(self, STCD: int, TM: str):
        return await self.dao.get_water_level(STCD, TM)
