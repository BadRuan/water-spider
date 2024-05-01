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
