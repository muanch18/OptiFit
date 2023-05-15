import numpy as np
import scipy.stats as stats

class StatisticalAnalysis:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def calculate_confidence_interval(self, confidence_level=0.95):
        se = np.std(self.data)/np.sqrt(len(self.data))
        return stats.t.interval(confidence_level, len(self.data)-1, loc=np.mean(self.data), scale=se)

    def calculate_goodness_of_fit(self):
        ss_res = np.sum((self.data - self.model)**2)
        ss_tot = np.sum((self.data - np.mean(self.data))**2)
        return 1 - (ss_res / ss_tot)
