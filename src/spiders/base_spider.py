from abc import ABCMeta, abstractmethod


class BaseSpider(metaclass=ABCMeta):

    @abstractmethod
    def set_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_response(self, *args, **kwargs):
        pass
