import yaml

class Setting(object):
    def __init__(self, filename: str) -> None:
        self.s = {}
        with open(filename, "r", encoding="utf-8") as f:
            self.s = yaml.load(f, Loader=yaml.SafeLoader)
    
    def __check(self) -> None:
        if self.s == {}:
            raise ValueError("配置文件读取失败")
    
    def getMysqlSetting(self) -> dict:
        self.__check()
        return self.s['mysql']
