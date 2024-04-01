import logging
from json import loads
from dao.waterlevel import WaterlevelDao

class WaterlevelService:
    def __init__(self, data: str) -> None:
        data_obj = loads(data)
        self.dao = WaterlevelDao()
        self.data_sw: list = data_obj['data_sw']
        self.count = {
            "all": len(self.data_sw),
            "exists": 0,
            "insert": 0
        }
        logging.info(f"从目标站点成功获取到{self.count['all']}条水位数据")
    
    # 检查水位数据是否存在
    def __checkDataExists(self, w) -> bool:
        d = self.dao
        data = d.get_water_level(int(w['STCD']), w['TM']) # 从数据库查询这个时间水位数据是否存在
        if data :
            return True
        else:
            return False
    
    # 保存水位数据到数据库
    def saveToDatabase(self):
        for w in self.data_sw:
            if self.__checkDataExists(w):
                self.count['exists'] = self.count['exists'] + 1
            else:
                self.dao.insert_water_level(int(w['STCD']), w['Z'], w['TM'] + ":00")
                self.count['insert'] = self.count['insert'] + 1
    
    # 返回水位数据保存处理结果字符串
    def reprot(self) -> str:
        message = f"处理{self.count['all']}条水位数据, 其中: 本地已存在{self.count['exists']}条水位数据, 实际新增{self.count['insert']}条水位数据."
        logging.info(message)