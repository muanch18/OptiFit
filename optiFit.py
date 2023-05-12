import yaml
import sys

# from funcFamily import FuncFamily
# from metric import Metric
# from costFunc import CostFunc
# from optimizer import Optimizer

def main():

    if len(sys.argv) != 2:
        sys.exit("Must include YAML file name")

    file_name = sys.argv[1]

    with open(file_name, 'r') as fstream:
        fstream_dict = yaml.safe_load(fstream)

# Will edit later
    # function = FuncFamily.create(fstream_dict['function']['name'], **fstream_dict['function']['params'])
    # metric = Metric.create(fstream_dict['metric']['name'])
    # costFunc = CostFunc(data, function, metric)
    # optimizer = Optimizer.create(fstream_dict['optimizer']['name'])


main()