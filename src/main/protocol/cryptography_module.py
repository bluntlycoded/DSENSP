class CryptographyModule:
    def __init__(self):
        self.parameters = [0.5, 0.5, 0.5]
    
    def update_parameters(self, params):
        self.parameters = params
    
    def evaluate_security(self):
        score = sum(self.parameters)
        return score / 3.0
