# A\* Search Algorithm (A Star) - Simple Explanation

In this small project I explain and use the A* search algorithm.  
A* is a famous search method that uses both cost and heuristic to find the best path or best solution.

It is better than normal BFS and DFS because it knows which direction is good to try next.

---

## What is A\* Search?

A\* uses two values:

- **g(n)** = cost from start to current node
- **h(n)** = heuristic (guess of cost to the goal)
- **f(n) = g(n) + h(n)**

A\* always picks the node that has the smallest **f(n)**.

This makes the search smart and fast.

---

## Why A\* Is Good?

- It finds the shortest path (if heuristic is good)
- It is faster than uniform-cost search
- It does not try useless branches
- Easy to understand after some practice

---

## Heuristic

Heuristic is just an estimation.  
For example, in grid problems we can use Manhattan distance.

If heuristic is:

- **good** → A\* is fast
- **bad** → A\* becomes slow

---

## Example Problem (Simple Grid)

We try to go from a start point (S) to a goal point (G) on a small grid.  
We only move: up, down, left, right.

A\* will check cells with the smallest f(n).

---

## Example Output

```
Path: [(0,0), (0,1), (1,1), (2,1), (2,2)]
```

---

## Advantages

- Very good performance
- Can find optimal path
- Uses logic (cost + heuristic)

---

## Disadvantages

- Needs good heuristic
- Can use a lot of memory
- Not perfect for every problem

---

## Conclusion

A\* is one of the best search algorithms because it mixes cost and heuristic.  
It is used in games, maps, pathfinding, robots, and many other fields.
