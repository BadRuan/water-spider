from typing import List
from core.model import Database, Station, Date_Range


# 数据库参数
DATABASE_DEV = Database(
    url="127.0.0.1", port=6041, user="root", password="123456", database="water"
)


# 控制请求数据时间长度范围 (单位: 天)
DATE_RANGE_LENGTH = Date_Range(init=20, normal=1)


# 设置获取最新数据请求时间间隔（单位: 分钟）
REQUEST_INTRVAL: int = 3


# 站点代码和名称
STATIONS: List[Station] = [
    Station(stcd=60115400, name="芜湖"),
    Station(stcd=62904500, name="凤凰颈闸下"),
    Station(stcd=62900700, name="裕溪闸下"),
    Station(stcd=62900600, name="裕溪闸上"),
    Station(stcd=62906500, name="清水"),
    Station(stcd=62905100, name="新桥闸上"),
]
