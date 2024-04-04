from service.station import StationService

class StationControll:
    def __init__(self) -> None:
        self.s = StationService()

    # 检查是否存在站点表
    def check_table_exists(self) -> bool:
        return self.s.check_table_exists()

    # 创建站点表和初始化站点数据
    def init_station(self):
        self.s.create_station_table()
        self.s.init_station()