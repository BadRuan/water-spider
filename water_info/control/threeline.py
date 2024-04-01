import logging
from service.threeline import ThreeLineService

class ThreelineControl:
    def __init__(self) -> None:
        pass
    
    def init_three(self):
        s = ThreeLineService()
        s.init_three_line()

    def get_all_three_line(self):
        s = ThreeLineService()
        for i in s.get_all_three_line_list():
            logging.info(i)