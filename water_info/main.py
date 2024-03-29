import random
from lib.decodeTool import DecodeStrTool
from api.getEncodeData import GetEncodeData

class App(object):
    def __init__(self) -> None:
        # self.MySQLTool = MySQLTool()
        self.api = GetEncodeData()

    # 展示本地MySQL数据库中的水位数据
    # def showWaterLevelDataOnDatabase(self) -> None:
    #     databse = self.MySQLTool
    #     r = databse.get_water_level(60115400, 10)
    #     for i in r:
    #         print(i)

    def decodeApiRequest(self):
        decode = DecodeStrTool()
        apiData = {
            "name": "2.1ZUdTdEx3bmlNZXBh",
            "stcd": "2.1MDYxMTQ1MDA=",
            "btime": "2.1MDI0MjMwMTA4MDAw",
            "etime": "2.1MDI0MjMwODI1MTAw",
            "sttp": "2.1UVo=",
            "waterEncode": "2.1cnRldQ==",
        }
        for d in apiData:
            print("字段" + d)
            print("秘文: "+apiData[d])
            data = decode.decrypt(apiData[d])
            print("明文: " + data)

    def getEncodeData(self):
        r = random.random()
        d = self.api.getData("51004350", "202403010800", "202403292000", str(random.random()))
        print(d)

if __name__ == '__main__':
    app = App()
    app.getEncodeData()