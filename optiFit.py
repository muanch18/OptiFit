import yaml
import sys

from funcFactory import FuncFactory
from metricFactory import MetricFactory
from CostFunction import CostFunction
from OptimizationTechniqueFactory import OptimizationTechniqueFactory
from dataImportExport import DataImportExport

def main():

    if len(sys.argv) != 3:
        sys.exit("Must include YAML file name and data file")

    yml_file = sys.argv[1]
    data_file = sys.argv[2]

    with open(yml_file, 'r') as fstream:
        dict = yaml.safe_load(fstream)
    
    dataImport = DataImportExport(data_file)
    data = dataImport.import_data()

    function = FuncFactory.create(dict['function']['name'], **dict['function']['params'])
    metric = MetricFactory.create(dict['metric']['name'])
    costFunc = CostFunction(data, function, metric)
    optimizer = OptimizationTechniqueFactory.create(dict['optimizer']['name'])


main()