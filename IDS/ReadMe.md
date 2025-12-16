# N-Queens Problem Using Iterative Deepening Search (IDS)

# Yousef Elgamal

In this project I try to solve the N-Queens problem using IDS.  
IDS means we try depth search but with increasing depth limit every time.  
It is like normal DFS but we restart many times with a bigger limit.

It is not the fastest way, but it is easy to understand and good for studying.

---

## What is the N-Queens Problem?

We want to put N queens on an N x N board.  
The queens should not attack each other.

They attack if they are in:

- same row
- same diagonal

(We put one queen per column so columns are already safe)

The important thing is to find a board with **zero attacks**.

---

## Why IDS?

I used IDS because:

- it is simple idea
- it does not use too much memory like normal DFS
- it tries all depths slowly
- I learned the algorithm and wanted to practice

---

## How IDS Works (Simple Idea)

1. Start with limit = 0
2. Run DFS but cannot go deeper than the limit
3. If no solution, increase limit by 1
4. Repeat until we find a valid board

This is why it is called **Iterative Deepening**.

---

## State Representation

I represent the board like this:

- each level in DFS = one column
- at each column I try to put a queen in any row
- I continue until I try all columns or reach depth limit

Example:
For N = 4  
State can look like:

```
[1, 3, 0, 2]
```

Which means queen in:

- column 0 → row 1
- column 1 → row 3
- column 2 → row 0
- column 3 → row 2

---

## Checking Attacks

I check if a new queen is safe by:

- no queen in same row
- no queen on same diagonal

If safe → continue  
If not safe → stop this branch

---

## Example Output

```
Solution: [1, 3, 0, 2]
```

---

## Advantages

- Very low memory use
- Easy to implement
- Good for learning tree search

---

## Disadvantages

- Slow for large N
- Repeats work many times
- More costly than other search methods

---

## Conclusion

IDS is a simple and clean way to search the N-Queens solution.  
It may not be the best algorithm, but it is useful for understanding search methods.
