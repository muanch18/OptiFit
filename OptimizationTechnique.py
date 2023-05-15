import abc

class OptimizationTechnique(abc.ABC):

    @abc.abstractmethod
    def __init__(self, cost_function):
        self.cost_function = cost_function

    @abc.abstractmethod
    def optimize(self):
        pass
