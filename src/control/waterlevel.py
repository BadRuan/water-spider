import logging
from config.settings import STATIONS
from service.waterlevel import WaterlevelService


class WaterlevelControl:
    def __init__(self) -> None:
        self.s = WaterlevelService()

    # 初始化水位信息表
    async def init_threeline(self):
        await self.s.create_waterlevel_table()

    # 保存水位信息到数据库中
    async def save_waterlevel_into_database(self, data: list):
        logging.info(f"数据库操作准备: 待处理{len(data)}条数据")
        count = 0
        for item in data:
            num = await self.s.insert_water_level(
                item["STCD"], float(item["Z"]), item["TM"]
            )
            count += num
        logging.info(f"数据库成功新增{count}条数据")

    # 首次运行加载保存数据
    async def first_load_waterlevel_datedata(self, data: list):
        logging.info("首次启动爬虫程序,准备获取今年内目标站点所有历史水位数据")
        await self.save_waterlevel_into_database(data)
        logging.info("今年内目标站点所有历史水位数据获取完成")
