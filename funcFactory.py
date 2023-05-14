from linReg import LinearRegression


class FuncFactory:

    def create(name, **params):
        functions = {'linReg' : LinearRegression}
        
        if name in functions:
            function = functions[name]
        else: 
            return None
        
        return function(**params)

