from service.station import StationService

class StationControll:
    def __init__(self) -> None:
        pass

    def init_station(self):
        s = StationService()
        s.initStation()