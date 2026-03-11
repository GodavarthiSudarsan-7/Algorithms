import random

N = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.1


def fitness(board):
    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                conflicts += 1
    return 28 - conflicts


def create_board():
    return [random.randint(0,7) for _ in range(N)]


def select(population):
    population.sort(key=lambda x: fitness(x), reverse=True)
    return population[:50]


def crossover(parent1, parent2):
    point = random.randint(1, N-1)
    return parent1[:point] + parent2[point:]


def mutate(board):
    if random.random() < MUTATION_RATE:
        i = random.randint(0,7)
        board[i] = random.randint(0,7)
    return board


def genetic_algorithm():
    population = [create_board() for _ in range(POPULATION_SIZE)]

    generation = 0

    while True:
        population = select(population)
        best = population[0]

        if fitness(best) == 28:
            return best, generation

        new_population = population.copy()

        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)

            child = crossover(parent1, parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population
        generation += 1



def print_board(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


solution, generation = genetic_algorithm()

print("Solution Found in Generation:", generation)
print("Queen Positions:", solution)
print("\nBoard Configuration:\n")

print_board(solution)