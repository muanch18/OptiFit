import numpy as np
from funcFamily import FuncFamily

class LogisticRegression(FuncFamily):
    def _func(self, x):
        num = np.e**(self.a + self.b * x)
        den = 1 + np.e**(self.a + self.b * x)
        return self.C * (num / den)

    def update_params(self, params):
        self.a = params[0]
        self.b = params[1]
        self.C = params[2]
    
    
    