import random

# Fitness Function
def fitness(state):
    attacks = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                attacks += 1
            if abs(state[i] - state[j]) == abs(i - j):
                attacks += 1

    return -attacks


# Tournament Selection
def select(pop):
    group = random.sample(pop, 3)
    return max(group, key=lambda c: fitness(c))


# One-Point Crossover
def crossover(a, b):
    point = random.randint(1, len(a) - 1)
    return a[:point] + b[point:]


# Mutation
def mutate(state, rate=0.1):
    if random.random() < rate:
        idx = random.randint(0, len(state) - 1)
        state[idx] = random.randint(0, len(state) - 1)
    return state


# Genetic Algorithm Main Loop
def solve_nqueens(n, pop_size=150, generations=2000):
    pop = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(pop_size)]

    for _ in range(generations):
        pop = sorted(pop, key=lambda c: fitness(c), reverse=True)

        if fitness(pop[0]) == 0:
            return pop[0]

        new_pop = []
        for _ in range(pop_size):
            parent1 = select(pop)
            parent2 = select(pop)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_pop.append(child)

        pop = new_pop

    return pop[0]


if __name__ == "__main__":
    solution = solve_nqueens(8)
    print("Solution:", solution)
