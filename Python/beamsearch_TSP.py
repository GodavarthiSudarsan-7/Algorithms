import heapq


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

N = len(graph)
beam_width = 2  

def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    return cost

def beam_search_tsp(start=0):
    beam = [[start]]  

    for _ in range(N - 1):
        candidates = []

        for path in beam:
            for city in range(N):
                if city not in path:
                    new_path = path + [city]
                    candidates.append(new_path)

   
        candidates.sort(key=lambda x: path_cost(x))

      
        beam = candidates[:beam_width]

    best_path = min(beam, key=lambda x: path_cost(x + [start]))
    best_path.append(start)

    return best_path, path_cost(best_path)

path, cost = beam_search_tsp()

print("Best Path:", path)
print("Total Cost:", cost)