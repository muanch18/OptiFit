import abc

class OptimizationTechnique(abc.ABC):

    @abc.abstractmethod
    def __init__(self, **params):
        pass

    @abc.abstractmethod
    def optimize(self, cost_function, initial_parameters):
        pass
