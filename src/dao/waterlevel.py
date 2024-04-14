from util.tdenginetool import TDengineTool
from config.settings import STATIONS2


class WaterlevelDao:
    def __init__(self) -> None:
        self.m = TDengineTool()

    # 创建水位数据表
    async def create_waterlevel_table(self) -> int:
        SQL = """CREATE TABLE IF NOT EXISTS `waterlevel` 
        (`ts` TIMESTAMP, `current` FLOAT) 
        TAGS (`STCD` INT, `NAME` BINARY(16))"""
        return await self.m.execute_sql(SQL)

    # 插入水位数据
    async def insert_water_level(self, waterlevels: list) -> int:
        SQL = f"""INSERT INTO t{waterlevels[0]['STCD']}
                USING waterlevel TAGS({waterlevels[0]['STCD']}, '{STATIONS2[waterlevels[0]["STCD"]]}')
                VALUES"""
        for item in waterlevels:
            SQL += f"('{item['TM']}:00.000', {item['Z']})"
        return await self.m.execute_sql(SQL)
