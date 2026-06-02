from typing import List, Tuple
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.model import DateSetting, Station


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql://user:pass@localhost:5432/dbname'
    TIMEZONE: str = 'UTC'
    
    model_config = SettingsConfigDict(
        env_file= '.env',
        env_file_encoding= 'utf-8',
        extra= 'ignore'
    )

settings = Settings()
    
type station_list_type = List[Tuple[int, str]]
     
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
