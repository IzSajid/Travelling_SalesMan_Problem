import itertools

class TravelingSalesmanBruteForce:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)

    def get_distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def solve(self):
        min_distance = float('inf')
        min_path = None

        for path in itertools.permutations(range(self.num_cities)):
            distance = 0
            for i in range(self.num_cities - 1):
                distance += self.get_distance(self.cities[path[i]], self.cities[path[i + 1]])
            distance += self.get_distance(self.cities[path[-1]], self.cities[path[0]])

            if distance < min_distance:
                min_distance = distance
                min_path = path

        return min_distance, [self.cities[i] for i in min_path]