# simple IDS solution for N-Queens
# written in a basic way

def safe(board, row, col):
    for c in range(col):
        if board[c] == row:
            return False
        if abs(board[c] - row) == abs(c - col):
            return False
    return True

def dfs(board, col, limit, n):
    if col == n:
        return board

    if col >= limit:
        return None

    for r in range(n):
        if safe(board, r, col):
            board[col] = r
            ans = dfs(board, col + 1, limit, n)
            if ans is not None:
                return ans
    return None

def ids(n):
    limit = 0
    while True:
        board = [-1] * n
        res = dfs(board, 0, limit, n)
        if res is not None:
            return res
        limit += 1

sol = ids(8)
print("Solution:", sol)