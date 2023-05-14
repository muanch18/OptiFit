from euclid import Euclidean


class MetricFactory:

    def create(name, **params):
        metrics = {'euclidean' : Euclidean}
        
        if name in metrics:
            metric = metrics[name]
        else: 
            return None
        
        return metric(**params)

