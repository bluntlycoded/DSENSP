import random
def tournament_selection(population, fitness_function, tournament_size=3):
    candidates = random.sample(population, tournament_size)
    candidates.sort(key=lambda chromo: fitness_function(chromo), reverse=True)
    return candidates[0]
