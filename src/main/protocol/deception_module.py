class DeceptionModule:
    def __init__(self):
        self.parameters = [0.5, 0.5, 0.5]
    
    def update_parameters(self, params):
        self.parameters = params
    
    def evaluate_deception(self):
        score = self.parameters[0] * self.parameters[1] * self.parameters[2]
        return score
