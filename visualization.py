import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, inputs, outputs, func):
        self.inputs = inputs
        self.outputs = outputs
        self.func = func

    def visualize(self):
        plt.plot(self.inputs, self.outputs)
        line = []
        for x in self.inputs:
            line.append(self.func(x))
        plt.plot(self.inputs, line)
        plt.show()