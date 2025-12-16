# simple A* search on a grid
# made as basic as possible

import heapq

def h(a, b):
    # manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, grid):
    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))
    came = {}
    g = {start: 0}

    while open_list:
        f, current = heapq.heappop(open_list)

        if current == goal:
            # build path
            path = []
            while current in came:
                path.append(current)
                current = came[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                newg = g[current] + 1
                if (nx, ny) not in g or newg < g[(nx, ny)]:
                    g[(nx, ny)] = newg
                    f2 = newg + h((nx, ny), goal)
                    heapq.heappush(open_list, (f2, (nx, ny)))
                    came[(nx, ny)] = current

    return None

grid = [
    [0,0,0],
    [1,0,0],
    [0,0,0]
]

path = astar((0,0), (2,2), grid)
print("Path:", path)
