class SimulationEngine:
    def __init__(self, crypto_module, routing_module, deception_module):
        self.crypto = crypto_module
        self.routing = routing_module
        self.deception = deception_module
    
    def simulate_protocol(self):
        security = self.crypto.evaluate_security()
        efficiency = self.routing.evaluate_routing()
        deception_score = self.deception.evaluate_deception()
        fitness = 0.4 * security + 0.4 * efficiency + 0.2 * deception_score
        return fitness
