from abc import ABC, abstractmethod

class ThreelineAbstract(ABC):

    # 创建水位三线表
    @abstractmethod
    def create_threeline_table(self) -> int:
        pass

    # 插入三线数据
    @abstractmethod
    def insert_three_line(self, STCD: int, SFSW: float, JJSW: float, BZSW: float,NAME: str) -> int:
        pass

    # 获取所有三线数据
    @abstractmethod
    def get_all_three_line_list(self) -> list:
        pass

