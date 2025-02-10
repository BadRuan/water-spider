from abc import ABCMeta, abstractmethod


class BaseParser(metaclass=ABCMeta):

    @abstractmethod
    def translate(self, *args, **kwargs):
        pass
