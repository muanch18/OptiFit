from euclid import Euclidean
from MeanSquaredError import MeanSquaredError


class MetricFactory:

    def create(name):
        metrics = {'euclidean' : Euclidean, 'mean squared' : MeanSquaredError}
        
        if name in metrics:
            metric = metrics[name]
        else: 
            return None
        
        return metric()

