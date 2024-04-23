from pydantic import BaseModel


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
