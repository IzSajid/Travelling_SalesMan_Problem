import heapq
import itertools

class TravelingSalesmanBranchAndBound:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.edges = {(i, j): self.get_distance(cities[i], cities[j]) for i in range(self.num_cities) for j in range(self.num_cities) if i != j}

    def get_distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def solve(self):
        heap = [(0, [0], set(range(1, self.num_cities)))]
        min_distance = float('inf')
        min_path = None

        while heap:
            lower_bound, path, remaining = heapq.heappop(heap)

            if not remaining:
                distance = sum(self.edges[(path[i], path[i + 1])] for i in range(self.num_cities - 1)) + self.edges[(path[-1], path[0])]

                if distance < min_distance:
                    min_distance = distance
                    min_path = path

            else:
                for city in remaining:
                    new_path = path + [city]
                    new_remaining = remaining - {city}
                    new_lower_bound = lower_bound + self.edges[(path[-1], city)]

                    if new_lower_bound < min_distance:
                        heapq.heappush(heap, (new_lower_bound, new_path, new_remaining))

        return min_distance, [self.cities[i] for i in min_path]