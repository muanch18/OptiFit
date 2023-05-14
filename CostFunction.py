class CostFunction:
    def __init__(self, y_true, y_pred, metric):
        self.y_true = y_true
        self.y_pred = y_pred
        self.metric = metric

    def cost(self):
        return self.metric(self.y_true, self.y_pred)
