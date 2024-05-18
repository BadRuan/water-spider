import logging
import asyncio
from typing import List
from core.dao import WaterLevelData
from core.settings import REQUEST_INTRVAL
from core.service import ApiService, insert_waterlevels


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)


class App:

    def __init__(self) -> None:
        self.service = ApiService()

    async def main(self):
        while True:
            await self.service.save_recently_data()
            await asyncio.sleep(REQUEST_INTRVAL * 60)

    async def save_target_year(self):
        target_year: int = 2022
        await self.service.save_target_year_datas(target_year)
        

    def start(self):
        asyncio.run(self.save_target_year())
