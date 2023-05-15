import numpy as np
import scipy.stats as stats

class StatisticalAnalysis:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def calculate_confidence_interval(self, confidence_level=0.95):
        se = np.std(self.data)/np.sqrt(len(self.data)) #standard error
        return stats.t.interval(confidence_level, len(self.data)-1, loc=np.mean(self.data), scale=se)
        # uses t distribution

    def calculate_goodness_of_fit(self): # for calculating r^2 val
        ss_res = np.sum((self.data - self.model)**2) # sum of the squares of the differences between the actual data and the model data
        ss_tot = np.sum((self.data - np.mean(self.data))**2) # sum of the squares of the differences between the actual data and the mean of the data
        return 1 - (ss_res / ss_tot) # calculates the R-squared value by subtracting the ratio, 1 indicates a perfect fit, while a value of 0 indicates no fit at all