import logging
from dao.database import MySQLTool
from config.settings import THREE_LINE

class ThreeLineService:
    def __init__(self) -> None:
        self.database = MySQLTool()
    
    def get_all_three_line_list(self) -> list:
        return self.database.get_all_three_line_list()
    
    def insert_three_line(self, STCD: int, SFSW: float, JJSW: float, BZSW: float,NAME: str) -> int:
        return self.database.insert_three_line(STCD, SFSW, JJSW, BZSW, NAME)
    
    def init_three_line(self):
        if len(self.get_all_three_line_list()) == 0:
            for i in THREE_LINE:
                self.insert_three_line(i['STCD'], i['SFSW'], i['JJSW'], i['BZSW'], i['NAME'])
                logging.info(f"创建 {i['NAME']} 三线水位信息")
        else:
            logging.error("已有三线水位信息, 初始化失败")