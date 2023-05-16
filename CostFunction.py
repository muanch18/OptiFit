
class CostFunction:
    def __init__ (self, data, funcFamily, metric):
        self.data = data
        self.funcFamily = funcFamily
        self.metric = metric
    
    def __call__(self, **params):
        return self.costFunc(**params)
    
    def costFunc(self, **params):
        func = self.funcFamily(**params)
        y_pred = func() #data input?
        return self.metric(y_pred) #data ouput?