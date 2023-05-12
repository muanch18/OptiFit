import abc

class FuncFamily(abc.ABC):

    @abc.abstractmethod
    def __init__(**params):
        pass

    @abc.abstractmethod
    def func(self, x):
        pass

    def __call__(self, x):
        return self.func(x)
    



