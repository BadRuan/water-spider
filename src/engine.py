import logging
import asyncio
from config.settings import REQUEST_INTRVAL
from service.waterlevel import WaterlevelService
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
        self.database = WaterlevelService()

    async def main(self):
        while True:
            data = await self.api.get_recently_data()
            for item in data:
                await self.database.insert_water_level(data[item])
            await asyncio.sleep(REQUEST_INTRVAL * 60)

    async def first_start(self):
        self.database.create_waterlevel_table()
        data = await self.api.get_year_datas()
        for item in data:
            await self.database.insert_water_level(data[item])

    def start(self):
        asyncio.run(self.main())
