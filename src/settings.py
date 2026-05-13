from typing import NamedTuple, List, Tuple, Generator
from model import DateSetting, Station


class DataConfig(NamedTuple):
    url: str
    user: str
    password: str
    port: int
    database: str
    
type station_list_type = List[Tuple[int, str]]

postgres = DataConfig(url='100.122.72.21', user='postgres', password='E,*f*YdGgYSgqfze1tLqc0Pm8CK2', port=36999, database='water') 
        
DATE_SETTINGS = DateSetting(latest_date_length=2, cut_date_length=20)

station_list: station_list_type = [
    (60115400,"芜湖"),
    (62904400,"凤凰颈新站闸上"),
    (62904500,"凤凰颈新站闸下"),
    (62900700,"裕溪闸下"),
    (62900600,"裕溪闸上"),
    (62906500,"清水"),
    (62905100,"新桥闸上")
]

stations = [Station(code=station[0], name=station[1], water_items=[]) for station in station_list]
