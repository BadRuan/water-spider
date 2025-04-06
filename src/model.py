from pydantic import BaseModel
from typing import List


class DatabaseConfig(BaseModel):
    url: str
    port: int
    user: str
    password: str
    database: str
    timezone: str


class StationConfig(BaseModel):
    stcd: int
    name: str


class RequestDateRange(BaseModel):
    btime: str
    etime: str


class WaterLevel(BaseModel):
    z: float
    tm: str


class DataWaterlevel(BaseModel):
    name: str
    stcd: int
    count: int
    data: List[WaterLevel]
