from linReg import LinearRegression
from logReg import LogisticRegression


class FuncFactory:

    def create(name, *params):
        functions = {
            'linReg' : LinearRegression,
            'logReg' : LogisticRegression
            }
        
        if name in functions:
            function = functions[name]
        else: 
            return None
        
        return function(*params)

