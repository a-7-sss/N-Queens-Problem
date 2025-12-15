# N‑Queens Solver Using Genetic Algorithm - Ahmed Mohamed Mohamed Hamada (C1 - 25)

This project demonstrates the use of a **Genetic Algorithm (GA)** to find a valid solution for the classical **N‑Queens puzzle**. The algorithm simulates evolutionary behavior such as selection, crossover, mutation, and survival of the fittest to progressively evolve toward a conflict‑free board configuration.

---

## 🔍 Overview of the N‑Queens Problem

The N‑Queens puzzle asks for placing **N queens** on an **N×N board** such that no two queens threaten each other.

Conflicts occur when queens share:

- The same row
- The same diagonal  
  (Columns are inherently unique in our representation)

---

## 🧬 Why a Genetic Algorithm?

GA is a strong candidate for this problem because:

- It handles huge combinatorial spaces well
- It does not require full state exploration
- It evolves solutions over generations
- It avoids exhaustive search
- It provides good solutions quickly

---

## 🧱 Representation

A board state is represented as a list of length **N**:

```
[state[0], state[1], ..., state[N-1]]
```

Where:

- Index = column
- Value = row of the queen

Example (N=8):

```
[2, 5, 1, 7, 4, 0, 6, 3]
```

---

## 📏 Fitness Evaluation

The fitness score is based on the number of **attacking pairs**.

A lower number of attacks = better fitness.  
A perfect solution yields **0 conflicts**.

---

## 🧲 Selection Method

We use **Tournament Selection**, which:

- Picks a small random group
- Selects the best chromosome as a parent
- Repeats to choose a second parent

This maintains strong candidates and preserves diversity.

---

## 🔗 Crossover Strategy

We apply a **One‑Point Crossover**:

- Select a random pivot
- Take prefix from Parent A
- Take suffix from Parent B

This blends features of both parents.

---

## 🔄 Mutation

Mutation modifies one random index to:

```
randint(0, N-1)
```

This helps avoid stagnation and improves diversity.

---

## 💻 Python Implementation

```python
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
```

---

## 🟢 Example Output

```
Solution: [4, 6, 1, 5, 2, 0, 3, 7]
```

---

## ⭐ Advantages

- Fast and efficient
- Handles huge search spaces
- Low memory usage
- Adaptable and flexible
- Good at escaping local minima

---

## ⚠️ Limitations

- No guarantee of best possible answer
- Quality depends on parameter tuning
- Randomness causes variation across runs

---

## 📊 Performance

| Metric         | Notes                                          |
| -------------- | ---------------------------------------------- |
| Execution Time | Typically < 0.5s for N=8                       |
| Memory Usage   | Low (population of small lists)                |
| Reliability    | High chance of reaching conflict‑free solution |
| Scalability    | Needs larger population for larger N           |

---

## ✔️ Conclusion

Genetic Algorithms provide an effective, flexible, and powerful method for solving the N‑Queens puzzle.  
The representation, operators, and evolutionary mechanisms combine to yield fast, high‑quality solutions.
