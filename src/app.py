from config.settings import Setting
from dao.database import MySQLTool
from tool.api import ApiTool 

class App(object):
    # 加载MySQL配置文件，连接MySQL数据库
    def __init__(self) -> None:
        databse_config = Setting('config/settings.yaml').getMysqlSetting()
        self.MySQLTool = MySQLTool(databse_config['host'], 
                                   databse_config['user'], 
                                   str(databse_config['password']), 
                                   databse_config['port'], 
                                   databse_config['database'])
    
    # 展示本地MySQL数据库中的水位数据
    def showWaterLevelDataOnDatabase(self) -> None:
        databse = self.MySQLTool
        r = databse.get_water_level(60115400, 10)
        for i in r:
            print(i)



if __name__ == '__main__':
    app = App()
    app.showWaterLevelDataOnDatabase()