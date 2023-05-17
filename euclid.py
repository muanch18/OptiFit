from metric import Metric
import numpy as np

class Euclidean(Metric):
    def __init__(self):
        pass
    
    def func(self, y, y_true):
        return np.sqrt((y - y_true)**2)
    
    