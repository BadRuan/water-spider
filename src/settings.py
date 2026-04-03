from typing import NamedTuple
from src.model import DateSetting, Station


class DataConfig(NamedTuple):
    url: str
    user: str
    password: str
    port: int
    database: str
    
postgres = DataConfig(url='100.95.218.64', user='postgres', password='E,*f*YdGgYSgqfze1tLqc0Pm8CK2', port=44455, database='water') 


DATE_SETTINGS = DateSetting(latest_date_length=2, cut_date_length=20)

STATIONS = [
    Station(code=60115400,name="芜湖",water_items=[]),
    # Station(code=62904400,name="凤凰颈闸下"),
    Station(code=62900700,name="裕溪闸下",water_items=[]),
    Station(code=62900600,name="裕溪闸上",water_items=[]),
    Station(code=62906500,name="清水",water_items=[]),
    Station(code=62905100,name="新桥闸上",water_items=[])
]