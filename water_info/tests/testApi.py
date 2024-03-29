from lib.decodeTool import DecodeStrTool
from lib.encodeTool import EncodeTool

class TestApi:
    # 将加密的txt文件转为解密的json文件
    def decodefile (self, input_file: str):
        d = EncodeTool()
        with open(input_file, "r", encoding="utf-8") as f:
            data: str = f.read()
            data = d.decrypt(data)
            output_file = input_file[:-4] + '.json'
            with open(output_file, "w", encoding="utf-8") as a:
                a.write(data)
            message = '成功：%s文件解译成功，目标文件名为%s' % (input_file, output_file)
            print(message)

    # 解密请求头参数
    def decodeApiRequest(self):
        decode = EncodeTool()
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
        
