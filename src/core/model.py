from pydantic import BaseModel


# 数据库参数格式
class Database(BaseModel):
    url: str
    port: int
    user: str
    password: str
    database: str


# 水文站参数格式
class Station(BaseModel):
    stcd: int
    name: str


# 控制爬虫请求数据的时间长度
class Date_Range(BaseModel):
    init: int
    normal: int


# 模型供保存API水位信息数据使用
class WaterLevelData(BaseModel):
    STCD: int
    Z: float
    TM: str


# 模型供查询水位数据使用
class WaterLevel(BaseModel):
    ts: str
    current: float
    stcd: int
    name: str
