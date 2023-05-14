import abc

class Metric(abc.ABC):

    @abc.abstractmethod
    def __init__(**params):
        pass

    @abc.abstractmethod
    def func(self, y, y_true):
        pass

    def __call__(self, y, y_true):
        return self.func(y, y_true)
    



