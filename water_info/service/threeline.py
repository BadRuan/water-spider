import logging
from dao.threeline import ThreelineDao
from config.settings import THREE_LINE

class ThreeLineService:
    def __init__(self) -> None:
        self.dao = ThreelineDao()
    
    # 创建站点三线水位表
    def create_threeline_table(self) -> int:
        return self.dao.create_threeline_table()
    
    # 获取所有站点三线水位信息
    def get_all_three_line_list(self) -> list:
        return self.dao.get_all_three_line_list()
    
    # 获取连接后的三线表
    def get_join_three_line_list(self) -> list:
        return self.dao.get_join_three_line_list()
    
    # 插入某站点三线水位信息
    def insert_three_line(self, STCD: int, SFSW: float, JJSW: float, BZSW: float,NAME: str) -> int:
        return self.dao.insert_three_line(STCD, SFSW, JJSW, BZSW, NAME)
    
    # 初始化：插入现有站点三线水位信息
    def init_three_line(self):
        if len(self.get_all_three_line_list()) == 0:
            for i in THREE_LINE:
                self.insert_three_line(i['STCD'], i['SFSW'], i['JJSW'], i['BZSW'], i['NAME'])
                logging.info(f"创建 {i['NAME']} 三线水位信息")
        else:
            logging.error("已有三线水位信息, 初始化失败")