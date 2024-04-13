import logging
import asyncio
from service.waterlevel import WaterlevelService
from service.api import ApiService

logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)


class App:

    async def main(self):
        api = ApiService()
        service = WaterlevelService()
        data = await api.get_recently_data()
        for i in data:
            await service.insert_water_level(data[i])

    # 正常启动项目采集水位信息功能，需要指定时间
    def start(self):
        asyncio.run(self.main())


if __name__ == "__main__":
    app = App()
    app.start()
