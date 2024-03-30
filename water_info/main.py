from dao.database import MySQLTool

class App(object):
    def __init__(self) -> None:
        self.database = MySQLTool()
    
    def get_all_station(self):
        l = self.database.get_all_station()
        for item in l:
            print(item)

if __name__ == '__main__':
    app = App()
    