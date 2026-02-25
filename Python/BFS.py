from collections import deque


initial_state = (
    (2, 4, 8),
    (3, 1, 7),
    (6, 5, 0)
)

goal_state = (
    (8, 1, 2),
    (7, 0, 3),
    (6, 5, 4)
)


moves = [(-1,0), (1,0), (0,-1), (0,1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_next_states(state):
    x, y = find_blank(state)
    next_states = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            next_states.append(tuple(tuple(row) for row in new_state))

    return next_states

def bfs():
    queue = deque([initial_state])
    visited = set([initial_state])
    parent = {initial_state: None}

    while queue:
        current = queue.popleft()

        if current == goal_state:
            return parent

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None

def print_solution(parent):
    path = []
    state = goal_state

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    print("Number of moves required:", len(path) - 1)
    print("\nStates from Initial to Goal:\n")

    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()


parent_map = bfs()
if parent_map:
    print_solution(parent_map)
else:
    print("Goal state not reachable.")
