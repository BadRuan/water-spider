from model import DateSetting, Station


DATE_SETTINGS = DateSetting(latest_date_length=2, cut_date_length=20)
STATIONS = [
    Station(code=60115400,name="芜湖"),
    Station(code=62904400,name="凤凰颈闸下"),
    Station(code=62900700,name="裕溪闸下"),
    # Station(code=62900600,name="裕溪闸上"),
    Station(code=62906500,name="清水"),
    Station(code=62905100,name="新桥闸上")
]