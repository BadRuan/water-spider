import logging
from service.threeline import ThreeLineService

class ThreelineControl:
    
    def init_threeline(self):
        s = ThreeLineService()
        s.create_threeline_table()
        s.init_three_line()

    def get_all_three_line(self):
        s = ThreeLineService()
        for i in s.get_all_three_line_list():
            logging.info(i)
