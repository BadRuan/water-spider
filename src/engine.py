import logging
import asyncio
from service.api import ApiService
from control.waterlevel import WaterlevelControl

logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)


class App:

    async def main(self):
        api_service = ApiService()
        waterlevel_control = WaterlevelControl()

        recently_data = await api_service.get_recently_data()
        await waterlevel_control.save_waterlevel_into_database(recently_data)

    # 正常启动项目采集水位信息功能，需要指定时间
    def start(self):
        asyncio.run(self.main())


if __name__ == "__main__":
    app = App()
    app.start()
