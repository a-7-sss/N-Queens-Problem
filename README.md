# Solving the N-Queens Problem Using Different AI Algorithms

This project is about solving the N-Queens problem using different Artificial Intelligence algorithms.
The main idea is to study the problem, apply several algorithms on it,
and then compare their performance to decide which one is more suitable.

---

## 1. Problem Description

The N-Queens problem is a well-known problem in Artificial Intelligence.
The task is to place N queens on an N × N chess board in a way that no two queens attack each other.

A queen attacks another queen if they are:
- in the same row
- in the same column
- in the same diagonal

In our implementations, we always place one queen per column,
so column conflicts are already avoided.
The main challenge is avoiding row and diagonal conflicts.

---

## 2. Why We Chose This Problem

We chose the N-Queens problem because:

- It is a classic AI problem
- It can be solved using many different algorithms
- It helps in understanding search and optimization techniques
- It is easy to test and visualize
- It allows comparison between informed, uninformed, and local search algorithms

This problem is suitable for learning and experimentation.

---

## 3. Algorithms Used in This Project

To solve the N-Queens problem, the following algorithms were used:

### 1. Depth First Search (DFS)
DFS places queens column by column and goes deep in one path.
If a conflict happens, it backtracks and tries another path.

---

### 2. Iterative Deepening Search (IDS)
IDS works like DFS but with a depth limit.
The limit increases step by step until a solution is found.
It combines low memory usage with complete search.

---

### 3. A* Search Algorithm
A* is an informed search algorithm.
It uses a heuristic function to guide the search toward better states.
This usually makes it faster than blind search algorithms.

---

### 4. Hill Climbing Algorithm
Hill Climbing is a local search algorithm.
It starts with a random solution and improves it step by step by reducing conflicts.
It is fast but can get stuck in local minima.

---

### 5. Genetic Algorithm (GA)
Genetic Algorithm is an optimization algorithm inspired by natural evolution.
It works with a population of solutions and improves them over generations using:
- selection
- crossover
- mutation

It is very useful for large search spaces and does not require checking all possibilities.

---

## 4. Comparison Between Algorithms

| Algorithm | Speed | Memory Usage | Always Finds Solution | Notes |
|---------|-------|--------------|----------------------|------|
| DFS | Slow for large N | Low | Yes | Simple but inefficient |
| IDS | Slower | Very Low | Yes | Repeats search many times |
| A* | Fast | High | Yes | Needs good heuristic |
| Hill Climbing | Very Fast | Very Low | No | Can get stuck |
| Genetic Algorithm | Fast | Medium | No | Depends on randomness |

---

## 5. Best Algorithm for Solving N-Queens

After applying and comparing all algorithms, we can conclude:

- **DFS and IDS** are good for learning and understanding basic search.
- **Hill Climbing** is fast but not reliable in all cases.
- **Genetic Algorithm** works well for large N and complex search spaces.
- **A\*** provides a good balance between speed and correctness but uses more memory.

### Final Choice:
For learning and explanation → **DFS / IDS**  
For performance and reliability → **A\***  
For optimization and large problems → **Genetic Algorithm**

Overall, **A\*** and **Genetic Algorithm** are the best choices depending on the problem size and requirements.

---

## 6. Team Members and Responsibilities

| Name | Responsibility |
|------|---------------|
| Ahmed Mohamed Rezk Abo Tahon | DFS implementation |
| Youssef Nasser Abdelsatar Elgamal | IDS implementation |
| Ahmed Mohamed Mostafa Abo Elkher | A* algorithm implementation |
| Ahmed Mohamed Mohamed Hamada | Genetic Algorithm implementation |
| Elsayed Ahmed Elsayed Rezk | Hill Climbing implementation |
| Ahmed Mohamed Mohamed Hamada | Testing, comparison, and documentation |


---

## 7. Conclusion

In this project, several Artificial Intelligence algorithms were applied to the N-Queens problem.
Each algorithm showed different behavior and performance.

This comparison helped us understand:
- how different search strategies work
- the strengths and weaknesses of each algorithm
- how to choose the best algorithm for a specific problem

Overall, this project was very useful for learning and practicing AI concepts in a practical way.
