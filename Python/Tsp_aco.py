import random

# Distance matrix
distance = [
    [0, 8, 5, 9],
    [8, 0, 6, 12],
    [5, 6, 0, 7],
    [9, 12, 7, 0]
]

num_cities = 4
num_ants = 5
iterations = 50
alpha = 1
beta = 2
evaporation = 0.5

pheromone = [[1 for _ in range(num_cities)] for _ in range(num_cities)]

def tour_length(tour):
    length = 0
    for i in range(len(tour)-1):
        length += distance[tour[i]][tour[i+1]]
    length += distance[tour[-1]][tour[0]]
    return length

best_tour = None
best_length = float('inf')

for _ in range(iterations):
    all_tours = []

    for ant in range(num_ants):
        tour = [random.randint(0, num_cities-1)]
        while len(tour) < num_cities:
            current = tour[-1]
            probs = []
            cities = []

            for city in range(num_cities):
                if city not in tour:
                    tau = pheromone[current][city] ** alpha
                    eta = (1 / distance[current][city]) ** beta
                    probs.append(tau * eta)
                    cities.append(city)

            total = sum(probs)
            probs = [p/total for p in probs]

            next_city = random.choices(cities, probs)[0]
            tour.append(next_city)

        all_tours.append(tour)

        length = tour_length(tour)
        if length < best_length:
            best_length = length
            best_tour = tour

    # pheromone evaporation
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1 - evaporation)

    # pheromone update
    for tour in all_tours:
        length = tour_length(tour)
        for i in range(len(tour)-1):
            a, b = tour[i], tour[i+1]
            pheromone[a][b] += 1/length
            pheromone[b][a] += 1/length

print("Best Tour:", [c+1 for c in best_tour] + [best_tour[0]+1])
print("Shortest Distance:", best_length)