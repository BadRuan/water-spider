from abc import ABC, abstractmethod

class StationAbstract(ABC):

    # 创建水文站表
    @abstractmethod
    def create_station_table(self) -> int:
        pass

    # 检查水文站表是否存在
    @abstractmethod
    def check_table_exists(self) -> int:
        pass

    # 插入水位站点代码
    @abstractmethod
    def insert_station(self, STCD: int, NAME: str) -> int:
        pass
    
    # 获取所有水位站点数据
    @abstractmethod
    def get_all_station(self) -> list:
        pass
