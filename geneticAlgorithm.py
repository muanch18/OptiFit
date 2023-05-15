from optimizationTechnique import OptimizationTechnique
from scipy.optimize import differential_evolution

class GeneticAlgorithm(OptimizationTechnique):
    def __init__(self, cost_function, bounds):
        super().__init__(cost_function)
        self.bounds = bounds

    def optimize(self, initial_parameters):
        result = differential_evolution(self.cost_function, self.bounds)
        return result.x, result.fun
