
import numpy as np
from OptimizationTechnique import OptimizationTechnique

class StochasticGradientDescent(OptimizationTechnique):
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.theta = None
        self.cost_history = []
    
    def optimize(self, cost_function, initial_parameters):
        self.theta = initial_parameters.copy()
        
        for _ in range(self.num_iterations):
            cost = cost_function(self.theta)
            self.cost_history.append(cost)
            
            gradient = self.compute_gradient(cost_function, self.theta)
            self.theta = self.theta - (self.learning_rate * gradient)
        
        return self.theta
    
    def compute_gradient(self, cost_function, theta):
        epsilon = 1e-7
        num_parameters = len(theta)
        gradient = np.zeros(num_parameters)
        
        for i in range(num_parameters):
            theta_plus = theta.copy()
            theta_minus = theta.copy()
            theta_plus[i] += epsilon
            theta_minus[i] -= epsilon
            
            gradient[i] = (cost_function(theta_plus) - cost_function(theta_minus)) / (2 * epsilon)
        
        return gradient
   


