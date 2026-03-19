from dataclasses import dataclass


@dataclass
class RequestDateRange:
    start_time: str
    end_time: str

    def __str__(self):
        return f"请求日期范围: {self.start_time} -> {self.end_time}"