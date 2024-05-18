import logging
from typing import List
from json import loads
from core.settings import STATIONS
from core.model import WaterLevelData
from util.tdenginetool import TDengineTool
from util.datetool import (
    DateRange,
    get_recently_time_range,
    get_target_year_date_range_list,
)
from util.apiTool import ApiTool
from util.encodeTool import EncodeTool


# 插入水位数据
async def insertWaterlevelToDdatabase(waterlevels: List[WaterLevelData]) -> int:
    with TDengineTool() as td:
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
        return td.execute(SQL)


class ApiDao:
    def __init__(self) -> None:
        self.api = ApiTool()
        self.tool = EncodeTool()

    # 获取响应数据
    async def __getResData(self, STCD: int, date_range: DateRange) -> str:
        tool = self.tool
        data = {
            "name": tool.encrypt("GetSwLineMap"),
            "stcd": tool.encrypt(str(STCD)),
            "btime": tool.encrypt(date_range.btime),
            "etime": tool.encrypt(date_range.etime),
            "sttp": tool.encrypt("ZQ"),
            "waterEncode": tool.encrypt("true"),
        }
        # 解决新桥闸上参数不一致问题
        if STCD == 62905100:
            data["name"] = tool.encrypt("GetSwLineAndZX")
            data["sttp"] = tool.encrypt("DD")
            data["zxstcd"] = tool.encrypt("62905200")
            data["zxsttp"] = tool.encrypt("ZZ")
        return await self.api.getResData(data)

    # 获取解密数据
    async def __getDecodeData(
        self, STCD: str, date_range: DateRange
    ) -> List[WaterLevelData]:
        data = await self.__getResData(STCD, date_range)
        json_obj = loads(data)
        if json_obj["respCode"] == "0":
            encodeData = json_obj["data"]
            data_str = self.tool.decrypt(encodeData)
            data_obj = loads(data_str)
            data_sw = data_obj["data_sw"]
            return [WaterLevelData(**i) for i in data_sw]
        else:
            logging.error(json_obj["respMsg"])

    # 获取最新水位数据
    async def get_recently_data(self, STCD: int) -> List[WaterLevelData]:
        return await self.__getDecodeData(STCD, get_recently_time_range())

    # 获取指定年份的所有水位数据
    async def get_target_year_datas(self, year: int, STCD: int) -> List[WaterLevelData]:
        year_data: List[WaterLevelData] = []
        for date_range in get_target_year_date_range_list(year):
            data = await self.__getDecodeData(STCD, date_range)
            for d in data:
                year_data.append(d)
        return year_data
