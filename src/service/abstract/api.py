from abc import ABC, abstractmethod


class ApiAbstract(ABC):

    # 获取最新水位数据
    @abstractmethod
    async def get_recently_data(self) -> list:
        pass


    # 获取指定时间的水位数据
    @abstractmethod
    async def get_target_data(
        self,
        input_datetime_str: str,
        days: int,
    ):
        pass

    # 初始化：获取今年所有水位数据
    @abstractmethod
    async def get_year_datas(self):
        pass