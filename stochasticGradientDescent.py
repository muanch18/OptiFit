from optimizationTechnique import OptimizationTechnique
from sklearn.linear_model import SGDRegressor


class StochasticGradientDescent(OptimizationTechnique):
    def __init__(self, learning_rate="constant", eta0=0.01, max_iter=1000, tol=1e-3):
        self.learning_rate = learning_rate
        self.eta0 = eta0
        self.max_iter = max_iter
        self.tol = tol

    def optimize(self, X, y):
        sgd = SGDRegressor(learning_rate=self.learning_rate, eta0=self.eta0, max_iter=self.max_iter, tol=self.tol)
        sgd.fit(X, y)
        return sgd.coef_, sgd.intercept_
