import yaml
import sys
import numpy as np
from funcFactory import FuncFactory
from metricFactory import MetricFactory
from CostFunction import CostFunction
from OptimizationTechniqueFactory import OptimizationTechniqueFactory
from dataImportExport import DataImportExport

def main():

    if len(sys.argv) != 2:
        sys.exit("Must include YAML file name")

    yml_file = sys.argv[1]
    with open(yml_file, 'r') as fstream:
        dict = yaml.safe_load(fstream)
    
    data_file = dict['data']['name']
    dataImport = DataImportExport(data_file)
    data = dataImport.import_data()

    x = dict['data']['params']['x']
    y = dict['data']['params']['y']
    inputs = np.array(data[x])
    outputs = np.array(data[y])

    metric = MetricFactory.create(dict['metric']['name'])

    func_params = dict['function']['params']
    initial_parameters = np.array(list(func_params.values()))

    func = FuncFactory.create(dict['function']['name'], initial_parameters)

    costFunc = CostFunction(inputs, outputs, func, metric)

    # dont know why line below doesnt compile...
    # optimizer = OptimizationTechniqueFactory.create(dict['optimizer']['name'], dict['optimizer']['params'])
    optimizer = OptimizationTechniqueFactory.create(dict['optimizer']['name'])
    
    result = optimizer.optimize(costFunc, initial_parameters)

    print(result)


main()