import logging
from json import loads
from dao.database import MySQLTool

class SaveDateService:
    def __init__(self, data: str) -> None:
        data_obj = loads(data)
        self.database = MySQLTool()
        self.data_sw: list = data_obj['data_sw']
        self.count = {
            "all": len(self.data_sw),
            "exists": 0,
            "insert": 0
        }
    
    # 检查水位数据是否存在
    def __checkDataExists(self, w) -> bool:
        d = self.database
        data = d.get_water_level(int(w['STCD']), w['TM']) # 从数据库查询这个时间水位数据是否存在
        if data :
            return True
        else:
            return False
    
    # 保存数据到数据库
    def saveToDatabase(self):
        for w in self.data_sw:
            if self.__checkDataExists(w):
                self.count['exists'] = self.count['exists'] + 1
            else:
                self.database.insert_water_level(int(w['STCD']), w['Z'], w['TM'] + ":00")
                self.count['insert'] = self.count['insert'] + 1
    
    # 返回处理结果字符串
    def reprot(self) -> str:
        message = '处理完%s条水位数据, 其中: %s条水位数据已存在, 实际新增%s条水位数据.' % (self.count['all'], self.count['exists'], self.count['insert'])
        logging.info(message)