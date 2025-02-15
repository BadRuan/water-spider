from abc import ABC, abstractmethod


# 观察者接口
class DataHandler(ABC):

    @abstractmethod
    def on_data_received(self, data):
        pass
