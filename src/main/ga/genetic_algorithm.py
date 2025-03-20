import random

class GeneticAlgorithm:
    def __init__(self, fitness_function, population_size=30, chromosome_length=9, mutation_rate=0.15, crossover_rate=0.8, chromosome_decoder=None):
        self.fitness_function = fitness_function
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.chromosome_decoder = chromosome_decoder
        self.population = self._initialize_population()
        self.generation_fitness = []
    
    def _initialize_population(self):
        return [[random.uniform(0, 1) for _ in range(self.chromosome_length)]
                for _ in range(self.population_size)]
    
    def _tournament_selection(self, tournament_size=3):
        candidates = random.sample(self.population, tournament_size)
        candidates.sort(key=lambda chromo: self.fitness_function(chromo), reverse=True)
        return candidates[0]
    
    def _crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            points = sorted(random.sample(range(1, self.chromosome_length), 2))
            child = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:]
            return child
        else:
            return parent1[:]
    
    def _mutate(self, chromosome):
        for i in range(self.chromosome_length):
            if random.random() < self.mutation_rate:
                chromosome[i] = random.uniform(0, 1)
        return chromosome
    
    def run(self, generations=50):
        best_overall = None
        best_fitness = float('-inf')
        for gen in range(generations):
            new_population = []
            for _ in range(self.population_size):
                parent1 = self._tournament_selection()
                parent2 = self._tournament_selection()
                child = self._crossover(parent1, parent2)
                child = self._mutate(child)
                new_population.append(child)
            self.population = new_population
            gen_best = max(self.population, key=lambda chromo: self.fitness_function(chromo))
            gen_best_fitness = self.fitness_function(gen_best)
            self.generation_fitness.append(gen_best_fitness)
            if gen_best_fitness > best_fitness:
                best_fitness = gen_best_fitness
                best_overall = gen_best
        return best_overall
