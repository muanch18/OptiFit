from funcFamily import FuncFamily
import numpy as np

class Exponential(FuncFamily):
    def _func(self, x):
        return self.a * np.e**(self.b * x)

    def update_params(self, params):
        self.a = params[0]
        self.b = params[1]
    
    
    