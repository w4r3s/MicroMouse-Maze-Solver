# modules/algorithm_parameters.py

class AlgorithmParameters:
    def __init__(self):
        self.parameters = {}

    def set_parameter(self, algorithm_name, param_name, value):
        if algorithm_name not in self.parameters:
            self.parameters[algorithm_name] = {}
        self.parameters[algorithm_name][param_name] = value

    def get_parameters(self, algorithm_name):
        return self.parameters.get(algorithm_name, {})
