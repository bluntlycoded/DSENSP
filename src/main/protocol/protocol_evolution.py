from ga.genetic_algorithm import GeneticAlgorithm
from network_simulation.simulation_engine import SimulationEngine
from protocol.cryptography_module import CryptographyModule
from protocol.routing_module import RoutingModule
from protocol.deception_module import DeceptionModule
from logging.logger import Logger

class ProtocolEvolution:
    def __init__(self, population_size=30, generations=50):
        self.logger = Logger()
        self.crypto = CryptographyModule()
        self.routing = RoutingModule()
        self.deception = DeceptionModule()
        self.simulation_engine = SimulationEngine(self.crypto, self.routing, self.deception)
        self.chromosome_length = 9
        self.ga = GeneticAlgorithm(
            fitness_function=self.evaluate_fitness,
            population_size=population_size,
            chromosome_length=self.chromosome_length,
            mutation_rate=0.15,
            crossover_rate=0.8,
            chromosome_decoder=self.decode_chromosome
        )
        self.generations = generations

    def decode_chromosome(self, flat_chromosome):
        return {
            "encryption": flat_chromosome[0:3],
            "routing": flat_chromosome[3:6],
            "deception": flat_chromosome[6:9]
        }

    def update_modules(self, candidate):
        self.crypto.update_parameters(candidate["encryption"])
        self.routing.update_parameters(candidate["routing"])
        self.deception.update_parameters(candidate["deception"])

    def evaluate_fitness(self, flat_chromosome):
        candidate = self.decode_chromosome(flat_chromosome)
        self.update_modules(candidate)
        fitness = self.simulation_engine.simulate_protocol()
        self.logger.log(f"[Evolution] Candidate: {candidate} Fitness: {fitness:.4f}")
        return fitness

    def evolve(self):
        self.logger.log("Starting protocol parameter evolution...")
        best_candidate = self.ga.run(self.generations)
        best_config = self.decode_chromosome(best_candidate)
        self.logger.log(f"[Evolution] Best configuration: {best_config}")
        return best_config

if __name__ == "__main__":
    evolution = ProtocolEvolution(population_size=30, generations=50)
    best_config = evolution.evolve()
    print("Best evolved configuration:", best_config)
