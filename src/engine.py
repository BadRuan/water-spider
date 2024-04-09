import logging
import asyncio
from config.settings import STATIONS
from dao.threeline import ThreelineDao

logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)

class App:
    
    def __init__(self) -> None:
        pass
    
    async def main(self):
        dao = ThreelineDao()
        tasks = []
        tasks.append(asyncio.create_task(dao.get_all_three_line_list()))
        await asyncio.wait(tasks)
        
            

    # 正常启动项目采集水位信息功能，需要指定时间
    def start(self):
        # asyncio.run()
        asyncio.run(self.main())


if __name__ == "__main__":
    app = App()
    app.start()
