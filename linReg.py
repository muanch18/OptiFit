from funcFamily import FuncFamily

class LinearRegression(FuncFamily):
    def __init__(self, m, b):
        self.m = m
        self.b = b
    
    def func(self, x):
        return self.m * x + self.b
    
    