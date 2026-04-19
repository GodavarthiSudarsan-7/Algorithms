from collections import deque


grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

rows = len(grid)
cols = len(grid[0])

moves = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs():
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            return parent

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

    return None


def print_path(parent):
    path = []
    node = goal

    while node:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Path from Start to Goal:")
    for step in path:
        print(step)



parent_map = bfs()

if parent_map:
    print_path(parent_map)
    print("Steps required:", len(parent_map))
else:
    print("No path found")