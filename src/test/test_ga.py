import unittest
from ga.genetic_algorithm import GeneticAlgorithm
def dummy_fitness(chromo):
    return sum(chromo)
class TestGeneticAlgorithm(unittest.TestCase):
    def test_initial_population(self):
        ga = GeneticAlgorithm(fitness_function=dummy_fitness, population_size=10, chromosome_length=5)
        self.assertEqual(len(ga.population), 10)
        self.assertEqual(len(ga.population[0]), 5)
    def test_run_evolution(self):
        ga = GeneticAlgorithm(fitness_function=dummy_fitness, population_size=10, chromosome_length=5)
        best = ga.run(generations=5)
        self.assertLessEqual(sum(best), 5)
if __name__ == "__main__":
    unittest.main()
