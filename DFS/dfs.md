# N-Queens Problem Using Depth First Search (DFS)

In this project I try to solve the N-Queens problem using Depth First Search (DFS).
DFS is a simple search algorithm that goes deep in one path before trying another path.

The idea is easy and good for learning basic search algorithms.

---

## What is the N-Queens Problem?

The N-Queens problem means placing N queens on a chess board (N x N).
The queens should not attack each other.

Queens attack if they are:

- in the same row
- in the same diagonal

I place one queen in each column, so columns are already safe.

---

## Why DFS?

I used DFS because:

- it is easy to understand
- simple to implement
- good for learning recursion
- does not need complex logic

---

## How DFS Works Here

- Each level of recursion represents one column
- In each column, I try all rows
- If the position is safe, I go deeper
- If not safe, I go back (backtracking)

---

## State Representation

The board is represented by a list.

Example for N = 4:
[1, 3, 0, 2]

Index = column  
Value = row of the queen

---

## Checking Safety

Before placing a queen, I check:

- no other queen in same row
- no other queen in same diagonal

If safe, continue DFS.

---

## Example Output

Solution: [1, 3, 0, 2]

---

## Advantages

- Very simple
- Easy to write
- Good for small N
- Helps understand backtracking

---

## Disadvantages

- Slow for large N
- Tries many wrong paths
- Uses recursion depth

---

## Conclusion

DFS is a basic search algorithm.
It is not the fastest solution for N-Queens, but it is useful for understanding search and backtracking.
