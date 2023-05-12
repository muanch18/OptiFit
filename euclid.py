from metric import Metric

class Euclidean(Metric):
    def __init__(self):
        pass
    
    def func(self, y, y_true):
        return (y - y_true)**2
    
    