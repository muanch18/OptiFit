from funcFamily import FuncFamily

class LinearRegression(FuncFamily):
    def _func(self, x):
        return self.m * x + self.b

    def update_params(self, params):
        self._params = params
        self.m = params[0]
        self.b = params[1]
    
    
    