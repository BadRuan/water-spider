from tool.dataTool import DataTool
from tool.decodeTool import DecodeTool

def decodefile (filename: str):
    d = DataTool()
    with open(filename + '.txt', "r", encoding="utf-8") as f:
        data: str = f.read()
        data = d.decrypt(data)
        with open(filename + '.json', "w", encoding="utf-8") as a:
            a.write(data)
        print("success")

def decodeApiRequest():
    decode = DecodeTool()
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
        


if __name__ == "__main__":
    decodeApiRequest()
    
    