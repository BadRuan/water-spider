from abc import ABC, abstractmethod

class WaterlevelAbstract(ABC):

    # 创建水位数据表
    @abstractmethod
    def create_waterlevel_table(self) -> int:
        pass

    # 插入某条水位数据
    @abstractmethod
    def insert_water_level(self, STCD: int, Z: float, TM: str) -> int:
        pass

    # 获取某站点指定数量的水位数据
    @abstractmethod
    def get_water_level_list(self, STCD: int, limit: int) -> list:
        pass

    # 获取指定时间的水位数据
    @abstractmethod
    def get_water_level(self, STCD: int, TM: str):
        pass