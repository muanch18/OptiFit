from metric import Metric
import numpy as np

class MeanSquaredError(Metric):
    def __init__(self):
        pass
    
    def func(self, y, y_true):
        return np.mean((y - y_true)**2)
