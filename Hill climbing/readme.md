# Solving N-Queens with Hill Climbing

In this project, I tried to solve the N-Queens problem using the Hill Climbing algorithm.
The idea here is not to make the best or fastest solution, but to understand how
local search algorithms work in a simple way.

Hill Climbing depends on improving the solution step by step until no better move is found.

---

## First: What is the N-Queens Problem?

The N-Queens problem is a classic problem in Artificial Intelligence.
The goal is to place N queens on an N x N chess board.

The important rule is:
No two queens are allowed to attack each other.

A queen can attack another queen if:

- they are in the same row
- they are in the same diagonal

In this project, each column has exactly one queen, so column conflicts do not exist.

---

## Why I Tried Hill Climbing

I chose Hill Climbing for this problem for some reasons:

- The algorithm is very easy to understand
- It does not need recursion like DFS
- It starts with a random solution, which is interesting
- It shows the idea of local search clearly

Hill Climbing does not search the whole space.
It only looks for better neighbors of the current state.

---

## General Idea of Hill Climbing

The algorithm works like this:

1. Start with a random board
2. Calculate how bad the board is (number of conflicts)
3. Try small changes on the board
4. If a change makes the board better, move to it
5. Repeat until no better solution is found

If the algorithm gets stuck, we restart with another random board.

---

## How the Board is Represented

The board is represented using a simple list.

- Index of the list = column number
- Value inside the list = row of the queen

Example for N = 8:

[3, 1, 6, 2, 5, 7, 0, 4]

This means:

- Queen in column 0 is in row 3
- Queen in column 1 is in row 1
- And so on...

---

## How the Evaluation Works

The evaluation function counts how many queens attack each other.
Every attacking pair increases the conflict count.

- More conflicts → bad board
- Less conflicts → better board
- Zero conflicts → solution found

The algorithm always tries to reduce this number.

---

## Result Example

After running the program, we may get something like:

Solution: [1, 3, 5, 7, 2, 0, 6, 4]
Conflicts: 0

This means the algorithm found a valid solution with no attacks.

---

## Things I Like About Hill Climbing

- Very simple logic
- Easy to code
- Fast in many cases
- Good for understanding local search

---

## Problems with Hill Climbing

- It can get stuck in a local minimum
- It does not guarantee a solution every time
- Needs random restarts to work better

---

## Final Notes

Hill Climbing is not a perfect algorithm.
However, it is a good example to understand how local search works.

This project helped me understand how small improvements can lead to a good solution.

