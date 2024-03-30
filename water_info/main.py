from lib.apiEncodeData import ApiEncodeData

class App(object):
    def __init__(self) -> None:
        self.api = ApiEncodeData()
    
    def getData(self):
        apiData = self.api.decodeToUsefulData('62904320', '202403201500')
        print(apiData)

if __name__ == '__main__':
    app = App()
    app.getData()