import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, inputs, outputs, func):
        self.inputs = inputs
        self.outputs = outputs
        self.func = func

    def visualize(self):
        plt.plot(self.inputs, self.outputs)
        plt.plot(self.inputs, self.func)
        plt.show()