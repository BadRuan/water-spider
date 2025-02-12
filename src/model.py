from pydantic import BaseModel
from typing import List


class ConfigDateRange(BaseModel):
    init: int
    normal: int


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
