import heapq


start = (
    (2, 8, 3),
    (1, 6, 4),
    (7, 0, 5)
)

goal = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

moves = [(-1,0), (1,0), (0,-1), (0,1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == value:
                            distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def astar():
    open_list = []
    heapq.heappush(open_list, (manhattan(start), 0, start))
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        _, cost, current = heapq.heappop(open_list)

        if current == goal:
            return parent

        for neighbor in get_neighbors(current):
            new_cost = cost + 1
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + manhattan(neighbor)
                heapq.heappush(open_list, (f_cost, new_cost, neighbor))
                parent[neighbor] = current

    return None

def print_solution(parent):
    path = []
    state = goal
    while state:
        path.append(state)
        state = parent[state]
    path.reverse()

    print("Number of moves required:", len(path) - 1)
    print("\nStates from Start to Goal:\n")

    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()


parent_map = astar()
if parent_map:
    print_solution(parent_map)
else:
    print("No solution found.")
