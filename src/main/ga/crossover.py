import random
def crossover(parent1, parent2, crossover_rate, chromosome_length):
    if random.random() < crossover_rate:
        points = sorted(random.sample(range(1, chromosome_length), 2))
        child = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:]
        return child
    else:
        return parent1[:]
