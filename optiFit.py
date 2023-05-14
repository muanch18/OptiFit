import yaml
import sys

from funcFactory import FuncFactory
# from metricFactory import MetricFactory
# from costFunc import CostFunc
# from optimizerFactory import OptimizerFactory

def main():

    if len(sys.argv) != 2:
        sys.exit("Must include YAML file name")

    file_name = sys.argv[1]

    with open(file_name, 'r') as fstream:
        dict = yaml.safe_load(fstream)

    function = FuncFactory.create(dict['function']['name'], **dict['function']['params'])

# Will edit later
    # metric = MetricFactory.create(dict['metric']['name'])
    # costFunc = CostFunc(data, function, metric)
    # optimizer = OptimizerFactory.create(dict['optimizer']['name'])


main()