from abc import ABCMeta, abstractmethod


class Figure:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        return 0

    @abstractmethod
    def __repr__(self):
        pass





