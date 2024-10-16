import math
import random

POPULATION = 100
GENERATIONS = 100
MUTATION_RATE = 0.5
CROSSOVER_RATE = 0.5
MIN_RANGE = -100
MAX_RANGE = 100


def fitness_function(x):
    return 0.05 * x**2 - 100 * math.cos(0.1 * x) + 120


def initialize_population():
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(POPULATION)]


def tournament_selection(population):
    best_candidate = random.choice(population)
    for _ in range(2):
        challenger = random.choice(population)
        if fitness_function(challenger) < fitness_function(best_candidate):
            best_candidate = challenger
    return best_candidate


def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        return (parent1 + parent2) / 2
    return parent1


def mutate(individual):
    if random.random() < MUTATION_RATE:
        return random.randint(MIN_RANGE, MAX_RANGE)
    return individual


def genetic_algorithm():
    population = initialize_population()

    for generation in range(GENERATIONS):
        new_population = []

        for _ in range(POPULATION):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring)
            new_population.append(offspring)

        population = new_population

        best_individual = min(population, key=fitness_function)
        print(f"Покоління {generation}: Найкраще x = {best_individual}, f(x) = {fitness_function(best_individual)}")

    return min(population, key=fitness_function)


if __name__ == "__main__":
    random.seed()
    best_solution = genetic_algorithm()
    print(f"Глобальний мінімум знайдено за x = {best_solution}, f(x) = {fitness_function(best_solution)}")
