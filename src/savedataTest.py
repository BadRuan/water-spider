from tool.database import DatabaseTool
import json

def saveTest():
    databse = DatabaseTool()
    row_num = 0
    with open('data.json', 'r', encoding="utf-8") as f:
        j = json.loads(f.read())
        data_sw = j['data_sw']
        for i in data_sw:
            row = databse.insert_water_level(int(i['STCD']), i['Z'], i['TM'])
            row_num = row_num + row
    databse.close()
    print(f"成功插入条{row_num}数据")

def getWaterLevelTest(num: int):
    databse = DatabaseTool()
    r = databse.get_water_level(60115400, num)
    for i in r:
        print(i)

if __name__ == "__main__":
    getWaterLevelTest(100)