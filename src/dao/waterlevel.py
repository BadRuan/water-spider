from typing import List
from config.settings import STATIONS
from util.tdenginetool import TDengineTool
from model.waterlevel import WaterLevelData


class WaterlevelDao:
    def __init__(self) -> None:
        self.m = TDengineTool()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int:
        SQL = """CREATE STABLE IF NOT EXISTS `waterlevel` 
                (`ts` TIMESTAMP, `current` FLOAT) 
                TAGS (`stcd` INT, `name` BINARY(16))"""
        return await self.m.execute_sql(SQL)

    # 插入水位数据
    async def insert_water_level(self, waterlevels: List[WaterLevelData]) -> int:
        stcd: int = waterlevels[0].STCD
        name = ""
        for station in STATIONS:
            if stcd == station.stcd:
                name = station.name
        SQL = f"""INSERT INTO t{waterlevels[0].STCD}
                USING waterlevel TAGS({waterlevels[0].STCD}, '{name}')
                VALUES"""
        for item in waterlevels:
            SQL += f"('{item.TM}:00.000', {item.Z})"
        return await self.m.execute_sql(SQL)

    # 查询当前最新水位
    async def select_cruuent_waterlevel(self) -> List[WaterLevelData]:
        SQL = "SELECT LAST_ROW(ts), `current`, `stcd`, `name` FROM waterlevel GROUP BY `stcd`"
        result = await self.m.query_fetch(SQL)
        return (
            WaterLevelData(ts=row[0], current=row[1], stcd=row[2], name=row[3])
            for row in result
        )
