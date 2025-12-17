# Simple DFS solution for N-Queens
# very basic and easy to understand

def safe(board, row, col):
    for c in range(col):
        if board[c] == row:
            return False
        if abs(board[c] - row) == abs(c - col):
            return False
    return True

def dfs(board, col, n):
    if col == n:
        return True

    for r in range(n):
        if safe(board, r, col):
            board[col] = r
            if dfs(board, col + 1, n):
                return True
            board[col] = -1
    return False

def solve(n):
    board = [-1] * n
    dfs(board, 0, n)
    return board

sol = solve(8)
print("Solution:", sol)
