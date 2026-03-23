from dataclasses import dataclass
from typing import NamedTuple, Optional, List


class DateSetting(NamedTuple):
    latest_date_length: int
    cut_date_length: int
    
    def __str__(self) -> str:
        return f"默认最近水位时间长度{self.latest_date_length}天, 整年水位切片时间 {self.cut_date_length}天."

class Station(NamedTuple):
    code: int
    name: str
    
    def __str__(self) -> str:
        return f"站点名称:{self.name} 站点代码:{self.code}"

@dataclass
class WaterLevel:
    height: float
    tm: str
    
    def __str__(self) -> str:
        return f"时间: {self.tm} => 高程: {self.height}"

@dataclass
class RequestDateRange:
    start_time: str
    end_time: str

    def __str__(self):
        return f"日期范围: {self.start_time} 至 {self.end_time}"
    
class Request:
    def __init__(self, station: Station, date_range: RequestDateRange):
        self.code: int = station.code
        self.name: str = station.name
        self.date_range: RequestDateRange = date_range
        self.encode_date: Optional[str] = None
        self.data: List[WaterLevel] = []

    def __str__(self) -> str:
        info: str = f"{self.name} 站水位数据"
        count: int = len(self.data)
        if count == 0 :
            info += f"载解析失败,"
        elif count > 0 :
            info += f"下载解析成功,共 {count} 条水位数据]"
        return info
    