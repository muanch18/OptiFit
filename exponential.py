from funcFamily import FuncFamily

class Exponential(FuncFamily):
    def _func(self, x):
        return self.a * (self.b ** x)

    def update_params(self, params):
        self.a = params[0]
        self.b = params[1]
    
    
    