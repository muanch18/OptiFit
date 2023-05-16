from stochasticGradientDescent import StochasticGradientDescent
from geneticAlgorithm import GeneticAlgorithm
#from meanVarianceOptimization import MeanVarianceOptimization

class OptimizationTechniqueFactory:
    def create(name, **params):
        techniques = {
            'sgd': StochasticGradientDescent,
            'genetic': GeneticAlgorithm,
        }
        
        if name in techniques:
            technique = techniques[name]
        else: 
            raise ValueError(f"Optimization technique {name} not recognized")
        
        return technique(**params)