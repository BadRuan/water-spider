from typing import List
from model.seetings import Database, Station, Date_Range


# 数据库参数
DATABASE_DEV = Database(
    url="127.0.0.1", port=6041, user="root", password="123456", database="water"
)


# 控制请求数据时间长度范围 (单位: 天)
DATE_RANGE_LENGTH = Date_Range(init=20, normal=1)


# 设置获取最新数据请求时间间隔（单位: 分钟）
REQUEST_INTRVAL: int = 5

# 站点代码和名称
STATIONS: List[Station] = [
    Station(stcd=60115400, name="芜湖"),
    Station(stcd=62904500, name="凤凰颈闸下"),
    Station(stcd=62900700, name="裕溪闸下"),
    Station(stcd=62900600, name="裕溪闸上"),
    Station(stcd=62906500, name="清水"),
    Station(stcd=62905100, name="新桥闸上"),
]


# 三线水位站点
THREE_LINE = [
    {
        "STCD": 62904400,
        "SFSW": 11.5,
        "JJSW": 13.2,
        "BZSW": 15.84,
        "NAME": "无为大堤",
    },
    {
        "STCD": 60115400,
        "SFSW": 9.4,
        "JJSW": 11.2,
        "BZSW": 13.4,
        "NAME": "城北圩",
    },
    {
        "STCD": 62900700,
        "SFSW": 8.7,
        "JJSW": 10.7,
        "BZSW": 12.7,
        "NAME": "江北（沈巷）长江堤",
    },
    {
        "STCD": 62906500,
        "SFSW": 10.1,
        "JJSW": 12.1,
        "BZSW": 14.1,
        "NAME": "万春圈堤",
    },
    {
        "STCD": 62900700,
        "SFSW": 9.4,
        "JJSW": 11.2,
        "BZSW": 12.3,
        "NAME": "裕溪口江堤",
    },
    {
        "STCD": 62900600,
        "SFSW": 9.5,
        "JJSW": 10.5,
        "BZSW": 12.0,
        "NAME": "裕溪河堤",
    },
    {
        "STCD": 62905100,
        "SFSW": 8.5,
        "JJSW": 9.5,
        "BZSW": 11.5,
        "NAME": "牛屯河堤",
    },
    {
        "STCD": 62904400,
        "SFSW": 11.5,
        "JJSW": 13.2,
        "BZSW": 14.5,
        "NAME": "惠生连圩堤",
    },
    {
        "STCD": 62904400,
        "SFSW": 11.5,
        "JJSW": 13.2,
        "BZSW": 15.84,
        "NAME": "永定大圩堤",
    },
    {
        "STCD": 62904400,
        "SFSW": 11.0,
        "JJSW": 13.0,
        "BZSW": 13.5,
        "NAME": "黑沙洲、天然洲圩",
    },
]
