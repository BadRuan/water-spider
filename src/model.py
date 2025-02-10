from pydantic import BaseModel


class ConfigDateRange(BaseModel):
    init: int
    normal: int


class RequestDateRange(BaseModel):
    btime: str
    etime: str
