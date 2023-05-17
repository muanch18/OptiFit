import abc

class FuncFamily(abc.ABC):

    def __init__(self, *params):
        self.update_params(*params)

    @abc.abstractmethod
    def _func(self, x):
        pass

    @abc.abstractmethod
    def update_params(self, *params):
        pass

    def __call__(self, x):
        return self._func(x)
    



