import random

# this function checks how many queens attack each other
def fitness(board):
    att = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j]:
                att += 1
            if abs(board[i] - board[j]) == abs(i - j):
                att += 1
    return att

# choose best from random 3
def select(pop):
    group = random.sample(pop, 3)
    best = group[0]
    for g in group:
        if fitness(g) < fitness(best):
            best = g
    return best

# crossover: take some from a and rest from b
def crossover(a, b):
    p = random.randint(1, len(a)-1)
    child = a[:p] + b[p:]
    return child

# random small change
def mutate(b):
    if random.random() < 0.1:
        i = random.randint(0, len(b)-1)
        b[i] = random.randint(0, len(b)-1)
    return b

def solve(n):
    pop = []
    for _ in range(100):
        board = [random.randint(0,n-1) for _ in range(n)]
        pop.append(board)

    for gen in range(2000):
        pop.sort(key=lambda x: fitness(x))
        if fitness(pop[0]) == 0:
            return pop[0]

        newpop = []
        for _ in range(100):
            p1 = select(pop)
            p2 = select(pop)
            c = crossover(p1, p2)
            c = mutate(c)
            newpop.append(c)
        pop = newpop

    return pop[0]


sol = solve(8)
print("Solution:", sol)
