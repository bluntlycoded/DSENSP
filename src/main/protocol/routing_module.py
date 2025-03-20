import math
class RoutingModule:
    def __init__(self):
        self.parameters = [0.5, 0.5, 0.5]
    
    def update_parameters(self, params):
        self.parameters = params
    
    def evaluate_routing(self):
        score = sum(self.parameters)
        return math.exp(-((score - 1.5) ** 2) / 0.1)
