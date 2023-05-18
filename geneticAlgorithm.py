from OptimizationTechnique import OptimizationTechnique
from scipy.optimize import differential_evolution

class GeneticAlgorithm(OptimizationTechnique):
    def __init__(self, bounds):
        self.bounds = bounds

    def optimize(self, cost_function, initial_parameters):
        result = differential_evolution(cost_function(initial_parameters), self.bounds)
        return result.x, result.fun
