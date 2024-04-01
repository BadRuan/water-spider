from service.station import StationService

class StationControll:

    def init_station(self):
        s = StationService()
        s.create_station_table()
        s.init_station()