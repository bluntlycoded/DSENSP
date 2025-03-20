import os
import json
import datetime
from ga.genetic_algorithm import GeneticAlgorithm
from network_simulation.simulation_engine import SimulationEngine
from protocol.cryptography_module import CryptographyModule
from protocol.routing_module import RoutingModule
from protocol.deception_module import DeceptionModule
from custom_logging.logger import Logger

class ProtocolManager:
    def __init__(self):
        self.logger = Logger()
        self.crypto = CryptographyModule()
        self.routing = RoutingModule()
        self.deception = DeceptionModule()
        self.simulation_engine = SimulationEngine(self.crypto, self.routing, self.deception)
        self.chromosome_length = 9
        self.ga = GeneticAlgorithm(
            fitness_function=self.evaluate_fitness,
            population_size=30,
            chromosome_length=self.chromosome_length,
            mutation_rate=0.15,
            crossover_rate=0.8,
            chromosome_decoder=self.decode_chromosome
        )
    
    def decode_chromosome(self, flat_chromosome):
        return {
            "encryption": flat_chromosome[0:3],
            "routing": flat_chromosome[3:6],
            "deception": flat_chromosome[6:9]
        }
    
    def update_protocol_modules(self, candidate):
        self.crypto.update_parameters(candidate["encryption"])
        self.routing.update_parameters(candidate["routing"])
        self.deception.update_parameters(candidate["deception"])
    
    def evaluate_fitness(self, flat_chromosome):
        candidate = self.decode_chromosome(flat_chromosome)
        self.update_protocol_modules(candidate)
        fitness = self.simulation_engine.simulate_protocol()
        self.logger.log(f"Evaluated candidate {candidate} with fitness: {fitness:.4f}")
        return fitness
    
    def run_evolution(self, generations=50):
        self.logger.log("Starting full evolution of network protocol...")
        best_candidate = self.ga.run(generations)
        best_config = self.decode_chromosome(best_candidate)
        final_fitness = self.evaluate_fitness(best_candidate)
        self.logger.log(f"Best protocol configuration evolved: {best_config}")
        self._save_results(best_config, final_fitness)
        return best_config
    
    def _save_results(self, best_config, final_fitness):
        result = {
            "timestamp": datetime.datetime.now().isoformat(),
            "run": int(datetime.datetime.now().timestamp()),
            "results": {
                "final_fitness": final_fitness,
                "protocol_parameters": best_config,
                "simulation_details": {
                    "dummy_duration": 1000,
                    "num_nodes": 50
                }
            }
        }
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "experiments", "simulation_results")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        filename = "results_" + datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + ".json"
        file_path = os.path.join(base_dir, filename)
        with open(file_path, "w") as f:
            json.dump(result, f, indent=4)
        self.logger.log(f"Simulation results saved to: {file_path}")

if __name__ == "__main__":
    pm = ProtocolManager()
    best_config = pm.run_evolution(generations=50)
    print("Best evolved protocol configuration:", best_config)
