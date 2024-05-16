import logging
import asyncio
from typing import List
from core.dao import WaterLevelData
from core.settings import REQUEST_INTRVAL
from core.service import ApiService, insert_waterlevels


logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)


class App:

    def __init__(self) -> None:
        self.api = ApiService()

    async def main(self):
        while True:
            data: List[WaterLevelData] = await self.api.get_recently_data()
            for item in data:
                await insert_waterlevels(data[item])
            await asyncio.sleep(REQUEST_INTRVAL * 60)

    async def first_start(self):
        data = await self.api.get_year_datas()
        for item in data:
            await insert_waterlevels(data[item])

    async def save_target_year(self):
        target_year: int = 2024
        data = await self.api.get_target_year_datas(target_year)
        for item in data:
            await insert_waterlevels(data[item])

    def start(self):
        asyncio.run(self.save_target_year())
