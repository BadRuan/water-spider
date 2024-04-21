from util.decodeTool import DecodeStrTool


def main():
    s = "2.1ZUdTdEx3bmlBZWRuWFo="
    tool = DecodeStrTool()
    print(tool.decrypt(s))


if __name__ == "__main__":
    main()
