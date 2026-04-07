from dataclasses import dataclass, field
from typing import NamedTuple, Optional, List


class DateSetting(NamedTuple):
    latest_date_length: int
    cut_date_length: int
    
class WaterItem(NamedTuple):
    height: float
    timestamp: str

class Station(NamedTuple):
    code: int
    name: str
    water_items: List[WaterItem]
        
class DateRange(NamedTuple):
    start_time: str
    end_time: str
    
@dataclass
class Request:
    code: int 
    name: str
    date_range: DateRange 
    encode_date: Optional[str] = None
    data: List[WaterItem] = field(default_factory=list)