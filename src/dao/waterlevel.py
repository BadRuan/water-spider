from util.tdenginetool import TDengineTool
from config.settings import STATIONS2
from pydantic import BaseModel
from typing import List
from dao.api import WaterLevelData


class WaterLevel(BaseModel):
    tm: str
    current: float
    stcd: int
    name: str


class WaterlevelDao:
    def __init__(self) -> None:
        self.m = TDengineTool()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int:
        SQL = """CREATE STABLE IF NOT EXISTS `waterlevel` 
        (`ts` TIMESTAMP, `current` FLOAT) 
        TAGS (`STCD` INT, `NAME` BINARY(16))"""
        return await self.m.execute_sql(SQL)

    # 插入水位数据
    async def insert_water_level(self, waterlevels: List[WaterLevelData]) -> int:
        SQL = f"""INSERT INTO t{waterlevels[0].STCD}
                USING waterlevel TAGS({waterlevels[0].STCD}, '{STATIONS2[str(waterlevels[0].STCD)]}')
                VALUES"""
        for item in waterlevels:
            SQL += f"('{item.TM}:00.000', {item.Z})"
        return await self.m.execute_sql(SQL)

    # 查询当前最新水位
    async def select_cruuent_waterlevel(self) -> List[WaterLevel]:
        SQL = "SELECT LAST_ROW(ts), `current`, `STCD`, `NAME` FROM waterlevel GROUP BY `STCD`"
        result = await self.m.query_fetch(SQL)
        return [
            WaterLevel(ts=row[0], current=row[1], stcd=row[2], name=row[3])
            for row in result
        ]
