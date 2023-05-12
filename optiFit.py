import yaml
import sys

# from funcFactory import FuncFactory
# from metricFactory import MetricFactory
# from costFunc import CostFunc
# from optimizerFactory import OptimizerFactory

def main():

    if len(sys.argv) != 2:
        sys.exit("Must include YAML file name")

    file_name = sys.argv[1]

    with open(file_name, 'r') as fstream:
        fstream_dict = yaml.safe_load(fstream)

# Will edit later
    # function = FuncFactory.create(fstream_dict['function']['name'], **fstream_dict['function']['params'])
    # metric = MetricFactory.create(fstream_dict['metric']['name'])
    # costFunc = CostFunc(data, function, metric)
    # optimizer = OptimizerFactory.create(fstream_dict['optimizer']['name'])


main()