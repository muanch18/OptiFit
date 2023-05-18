import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, inputs, outputs, func, input_name = 'input', output_name = 'output'):
        self.inputs = inputs
        self.outputs = outputs
        self.func = func
        self.input_name = input_name
        self.output_name = output_name

    def visualize(self):
        plt.scatter(self.inputs, self.outputs, label='Original Data', c = 'b')

        best_fit = np.zeros(len(self.inputs))
        for i in range(len(self.inputs)):
            best_fit[i] = self.func(self.inputs[i])

        plt.plot(self.inputs, best_fit, label="Best Fitted Data", c='r')
        plt.title('Best Fit for ' + self.input_name + ' vs. ' + self.output_name)
        plt.xlabel(self.input_name)
        plt.ylabel(self.output_name)
        plt.legend()
        plt.show()