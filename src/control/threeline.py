import logging
from service.threeline import ThreeLineService

class ThreelineControl:
    
    # 初始化三线数据
    async def init_threeline(self):
        s = ThreeLineService()
        await s.create_threeline_table()
        await s.init_three_line()

    # 获取所有三线数据
    async def get_all_three_line(self):
        s = ThreeLineService()
        for i in await s.get_all_three_line_list():
            logging.info(i)
