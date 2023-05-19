from linReg import LinearRegression
from exponential import Exponential


class FuncFactory:

    def create(name, *params):
        functions = {
            'linReg' : LinearRegression,
            'exponential' : Exponential
            }
        
        if name in functions:
            function = functions[name]
        else: 
            return None
        
        return function(*params)

