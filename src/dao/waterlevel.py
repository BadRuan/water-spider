from typing import List
from config.settings import STATIONS
from util.tdenginetool import TDengineTool
from model.waterlevel import WaterLevelData


# 插入水位数据
async def insert_water_level(waterlevels: List[WaterLevelData]) -> int:
    with TDengineTool() as connect:

        stcd: int = waterlevels[0].STCD
        name = ""
        # 从水文站配置信息中找出站点名
        for station in STATIONS:
            if stcd == station.stcd:
                name = station.name
        SQL = f"""INSERT INTO t{stcd}
                USING waterlevel TAGS({stcd}, '{name}')
                VALUES"""
        for item in waterlevels:
            SQL += f"('{item.TM}:00.000', {item.Z})"
        return connect.execute(SQL)
