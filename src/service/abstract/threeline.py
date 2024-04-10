from abc import ABC, abstractmethod


class ThreelineAbstract(ABC):

    # 创建站点三线水位表
    @abstractmethod
    async def create_threeline_table(self) -> int:
        pass

    # 获取所有站点三线水位信息
    @abstractmethod
    async def get_all_three_line_list(self) -> list:
        pass

    # 插入某站点三线水位信息
    @abstractmethod
    async def insert_three_line(
        self, STCD: int, SFSW: float, JJSW: float, BZSW: float, NAME: str
    ) -> int:
        pass

    # 初始化：插入现有站点三线水位信息
    @abstractmethod
    async def init_three_line(self):
        pass
