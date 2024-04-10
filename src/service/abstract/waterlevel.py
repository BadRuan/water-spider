from abc import ABC, abstractmethod


class WaterlevelAbstract(ABC):


    # 创建水位数据表
    @abstractmethod
    async def create_waterlevel_table(self) -> int:
        pass