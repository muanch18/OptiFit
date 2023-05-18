from OptimizationTechnique import OptimizationTechnique
from scipy.optimize import differential_evolution

class GeneticAlgorithm(OptimizationTechnique):
    def __init__(self, bounds):
        self.bounds = []
        for key in bounds:
            self.bounds.append((bounds[key]['min'], bounds[key]['max']))

    def optimize(self, cost_function, initial_parameters):
        result = differential_evolution(cost_function, self.bounds)
        return result.x
