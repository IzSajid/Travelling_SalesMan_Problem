import numpy as np

class TravelingSalesmanNearestNeighbor:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)

    def get_distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def solve(self):
        unvisited_cities = set(range(self.num_cities))
        current_city = np.random.choice(range(self.num_cities))
        path = [current_city]
        unvisited_cities.remove(current_city)
        total_distance = 0

        while unvisited_cities:
            nearest_city = min(unvisited_cities, key=lambda city: self.get_distance(self.cities[current_city], self.cities[city]))
            path.append(nearest_city)
            unvisited_cities.remove(nearest_city)
            total_distance += self.get_distance(self.cities[current_city], self.cities[nearest_city])
            current_city = nearest_city

        total_distance += self.get_distance(self.cities[path[-1]], self.cities[path[0]])

        return total_distance, [self.cities[i] for i in path]
