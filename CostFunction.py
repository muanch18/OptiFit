
class CostFunction:
    def __init__(self, inputs, outputs, func, metric):
        self.inputs = inputs
        self.outputs = outputs
        self.func = func
        self.metric = metric
    
    def __call__(self, *params):
        return self.costFunc(*params)
    
    def costFunc(self, *params):
        self.func.update_params(*params)
        y_pred = self.func(self.inputs)
        return self.metric(y_pred, self.outputs)