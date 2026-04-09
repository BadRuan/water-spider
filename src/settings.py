from typing import NamedTuple, List, Tuple
from model import DateSetting, Station
from os import getenv


class DataConfig(NamedTuple):
    url: str
    user: str
    password: str
    port: int
    database: str
    

def get_database_config(debug: bool = False) -> DataConfig:
    host: str = ''
    user: str = ''
    password: str = ''
    port: int = 5432
    
    if debug == False:
        _host = getenv('POST_HOST')
        _user = getenv('POST_USER')
        _password = getenv('POST_PASS')
        _port = getenv('POST_PORT')
        if _host is not None and _user is not None and _password is not None and _port is not None:
            host, user, password, port = _host, _user, _password, int(_port)
            return DataConfig(url=host, user=user, password=password, port= port, database='water')
        else:
            return DataConfig(url='100.95.218.65', user='postgres', password='E,*f*YdGgYSgqfze1tLqc0Pm8CK2', port=44455, database='water') 
    else:
        return DataConfig(url='100.95.218.65', user='postgres', password='E,*f*YdGgYSgqfze1tLqc0Pm8CK2', port=44455, database='water') 
        

DATE_SETTINGS = DateSetting(latest_date_length=2, cut_date_length=20)

station_list: List[Tuple[int, str]] = [
    (60115400,"芜湖"),
    (62904400,"凤凰颈新站闸上"),
    (62904500,"凤凰颈新站闸下"),
    (62900700,"裕溪闸下"),
    (62900600,"裕溪闸上"),
    (62906500,"清水"),
    (62905100,"新桥闸上")
]

STATIONS = [Station(code=station[0], name=station[1], water_items=[]) for station in station_list]
