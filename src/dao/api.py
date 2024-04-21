import logging
from typing import List
from json import loads
from pydantic import BaseModel
from config.settings import DATE_RANGE_LENGTH
from util.datetool import (
    DateRange,
    get_recently_time_range,
    get_time_range,
    get_init_data_range_list,
)
from util.apiTool import ApiTool
from util.encodeTool import EncodeTool


class WaterLevelData(BaseModel):
    STCD: int
    Z: float
    TM: str


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
        logging.debug("请求参数: ", data)
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

    # 获取指定时间的水位数据
    async def get_target_data(
        self,
        STCD: int,
        input_datetime_str: str,
        days: int = DATE_RANGE_LENGTH["normal"],
    ) -> List[WaterLevelData]:
        return await self.__getDecodeData(
            STCD, get_time_range(input_datetime_str, days)
        )

    # 初始化：获取今年所有水位数据
    async def get_year_datas(self, STCD: int) -> List[WaterLevelData]:
        year_data: List[WaterLevelData] = []
        for date_range in get_init_data_range_list():
            data = await self.__getDecodeData(STCD, date_range)
            for d in data:
                year_data.append(d)
        return year_data
