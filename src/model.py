from dataclasses import dataclass
from typing import NamedTuple, Optional, List


class DateSetting(NamedTuple):
    latest_date_length: int
    cut_date_length: int

class Station(NamedTuple):
    code: int
    name: str

@dataclass
class WaterLevel:
    height: float
    tm: str

@dataclass
class RequestDateRange:
    start_time: str
    end_time: str

    def __str__(self):
        return f"日期范围: {self.start_time} -> {self.end_time}"
    
class Request:
    def __init__(self, station: Station, date_range: RequestDateRange):
        self.code: int = station.code
        self.name: str = station.name
        self.date_range: RequestDateRange = date_range
        self.encode_date: Optional[str] = None
        self.data: List[WaterLevel] = []

    def __str__(self) -> str:
        return f"{self.name}站[{self.code}] {self.date_range.start_time}->{self.date_range.end_time} 共 {len(self.data)} 条水位数据]"