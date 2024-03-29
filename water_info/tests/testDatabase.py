import json
from dao.database import MySQLTool
from config.settings import Setting

class DatabaseTest(object):
    def __init__(self) -> None:
        m = Setting('settings.yaml').getMysqlSetting()
        self.MySQLTool = MySQLTool(m['host'], m['user'], str(m['password']), m['port'], m['database'])

    def saveTest(self):
        databse = self.MySQLTool
        row_num = 0
        with open('data.json', 'r', encoding="utf-8") as f:
            j = json.loads(f.read())
            data_sw = j['data_sw']
            for i in data_sw:
                row = databse.insert_water_level(int(i['STCD']), i['Z'], i['TM'])
                row_num = row_num + row
        databse.close()
        print(f"成功插入条{row_num}数据")

    def getWaterLevelTest(self,num: int):
        databse = self.MySQLTool
        r = databse.get_water_level(60115400, num)
        for i in r:
            print(i)

if __name__ == "__main__":
    d = DatabaseTest()
    d.getWaterLevelTest(20)