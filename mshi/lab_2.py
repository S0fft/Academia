import math
import random

POPULATION_SIZE = 100
MAX_GENERATIONS = 100
MUTATION_PROBABILITY = 0.5
CROSSOVER_PROBABILITY = 0.5
MIN_VALUE = -100
MAX_VALUE = 100


def calculate_fitness(x):
    return 0.05 * x**2 - 100 * math.cos(0.1 * x) + 120


def create_initial_population():
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(POPULATION_SIZE)]


def select_parent_by_tournament(population):
    best_individual = random.choice(population)
    for _ in range(2):
        competitor = random.choice(population)
        if calculate_fitness(competitor) < calculate_fitness(best_individual):
            best_individual = competitor
    return best_individual


def perform_crossover(parent1, parent2):
    if random.random() < CROSSOVER_PROBABILITY:
        return (parent1 + parent2) / 2
    return parent1


def apply_mutation(individual):
    if random.random() < MUTATION_PROBABILITY:
        return random.randint(MIN_VALUE, MAX_VALUE)
    return individual


def run_genetic_algorithm():
    population = create_initial_population()

    for generation in range(MAX_GENERATIONS):
        new_population = []

        for _ in range(POPULATION_SIZE):
            parent1 = select_parent_by_tournament(population)
            parent2 = select_parent_by_tournament(population)
            offspring = perform_crossover(parent1, parent2)
            offspring = apply_mutation(offspring)
            new_population.append(offspring)

        population = new_population

        best_individual = min(population, key=calculate_fitness)
        print(f"Покоління {generation}: Найкраще x = {best_individual}, f(x) = {calculate_fitness(best_individual)}")

    return min(population, key=calculate_fitness)


if __name__ == "__main__":
    random.seed()
    best_solution = run_genetic_algorithm()
    print(f"Глобальний мінімум знайдено за x = {best_solution}, f(x) = {calculate_fitness(best_solution)}")
