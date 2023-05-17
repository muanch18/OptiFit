import yaml
import sys
import numpy as np
from funcFactory import FuncFactory
from metricFactory import MetricFactory
from OptimizationTechniqueFactory import OptimizationTechniqueFactory
from dataImportExport import DataImportExport

def cost_function(params, model_func, metric_func, x, y_true):
    y_pred = model_func(params, x)
    return metric_func(y_pred, y_true)



def main():

    if len(sys.argv) != 2:
        sys.exit("Must include YAML file name")

    yml_file = sys.argv[1]
    with open(yml_file, 'r') as fstream:
        dict = yaml.safe_load(fstream)
    
    data_file = dict['data']['name']
    dataImport = DataImportExport(data_file)
    data = dataImport.import_data()

    function = FuncFactory.create(dict['function']['name'], **dict['function']['params'])

    metric = MetricFactory.create(dict['metric']['name'])

    data = DataImportExport.import_data(dict['data']['file_name'])

    x = np.array(data['x'])
    y_true = np.array(data['y'])

    optimizer = OptimizationTechniqueFactory.create(dict['optimizer']['name'], cost_function, function, metric, x, y_true)

    result = optimizer.optimize()
# Will edit later
    # metric = MetricFactory.create(dict['metric']['name'])
    # costFunc = CostFunc(data, function, metric)
    # optimizer = OptimizerFactory.create(dict['optimizer']['name'])



main()