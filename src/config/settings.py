from typing import List
from model import DatabaseConfig, StationConfig


DATABASE_DEV = DatabaseConfig(
    url="192.168.3.2", port=6041, user="root", password="Deepseek666", database="water"
)

# 默认请求日期范围
DEFAULT_DATE_RANGE: int = 2
INIT_DATE_RANGE: int = 25

# 站点代码和名称
STATIONS: List[StationConfig] = [
    StationConfig(stcd=60115400, name="芜湖"),
    StationConfig(stcd=62904500, name="凤凰颈闸下"),
    StationConfig(stcd=62900700, name="裕溪闸下"),
    StationConfig(stcd=62900600, name="裕溪闸上"),
    StationConfig(stcd=62906500, name="清水"),
    StationConfig(stcd=62905100, name="新桥闸上"),
]
