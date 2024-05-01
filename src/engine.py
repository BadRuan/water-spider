import logging
import asyncio
from typing import List
from dao.api import WaterLevelData
from config.settings import REQUEST_INTRVAL
from service.waterlevel import insert_waterlevels
from service.api import ApiService


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

    def start(self):
        asyncio.run(self.main())
