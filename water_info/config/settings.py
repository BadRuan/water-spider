# 数据库参数
DATABASE_CONFIG = {
    "dev": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "123456",
        "port": 3306,
        "database": "water"
    }
}

# 控制请求数据时间长度范围 单位为天
DATE_RANGE_LENGTH = 10

# 站点代码和名称
STATIONS = [
    {
        "STCD": 60115400,
        "NAME": "芜湖"
    },
    {
        "STCD": 62904400,
        "NAME": "凤凰颈闸下"
    },
    {
        "STCD": 62900700,
        "NAME": "裕溪闸下"
    },
    {
        "STCD": 62900600,
        "NAME": "裕溪闸上"
    },
    {
        "STCD": 62906500,
        "NAME": "清水"
    },
    {
        "STCD": 62905100,
        "NAME": "新桥闸上"
    }
]