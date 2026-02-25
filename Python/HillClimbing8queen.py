import random

N = 8


def heuristic(state):
    attacks = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks


def get_neighbors(state):
    neighbors = []
    for row in range(N):
        for col in range(N):
            if state[row] != col:
                new_state = list(state)
                new_state[row] = col
                neighbors.append(new_state)
    return neighbors


def hill_climbing():
    current = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current_h = heuristic(current)
        neighbors = get_neighbors(current)

        next_state = current
        next_h = current_h

        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < next_h:
                next_state = neighbor
                next_h = h

        if next_h >= current_h:
            return current, current_h

        current = next_state


def print_board(state):
    for i in range(N):
        for j in range(N):
            if state[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


solution, h_value = hill_climbing()

print("Final State:", solution)
print("Heuristic Value:", h_value)
print("\nBoard Configuration:\n")
print_board(solution)
