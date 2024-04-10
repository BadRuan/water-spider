from abc import ABC, abstractmethod


class StationAbstract(ABC):

    # 检查水文站表是否存在
    @abstractmethod
    async def check_table_exists(self) -> bool:
        pass

    # 创建水文站表
    @abstractmethod
    async def create_station_table(self) -> int:
        pass

    # 初始化：插入现有水文站点信息
    @abstractmethod
    async def init_station(self):
        pass
