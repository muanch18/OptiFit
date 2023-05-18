from metric import Metric
import numpy as np

class Euclidean(Metric):
    def __init__(self):
        pass
    
    def func(self, y_pred, y_true):
        return np.linalg.norm(np.sqrt((y_pred - y_true)**2))
    
    
    