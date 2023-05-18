from linReg import LinearRegression
from logReg import LogisticRegression
from exponential import Exponential


class FuncFactory:

    def create(name, *params):
        functions = {
            'linReg' : LinearRegression,
            'logReg' : LogisticRegression,
            'exponential' : Exponential
            }
        
        if name in functions:
            function = functions[name]
        else: 
            return None
        
        return function(*params)

