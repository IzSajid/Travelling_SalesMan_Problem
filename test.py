from brute_force import TravelingSalesmanBruteForce
from brarch_and_bound import TravelingSalesmanBranchAndBound
from nearest_neighbor import TravelingSalesmanNearestNeighbor
def main():
    # Test data: 5 cities at random locations
    cities = [(10, 10), (20, 30), (55, 25), (70, 48), (40, 60)]

    # Solve the TSP using brute force
    tsp_bf = TravelingSalesmanBruteForce(cities)
    min_distance_bf, min_path_bf = tsp_bf.solve()

    # Solve the TSP using branch and bound
    tsp_bb = TravelingSalesmanBranchAndBound(cities)
    min_distance_bb, min_path_bb = tsp_bb.solve()

    # Solve the TSP using nearest neighbor
    tsp_nn = TravelingSalesmanNearestNeighbor(cities)
    min_distance_nn, min_path_nn = tsp_nn.solve()

    # Print the result brute force
    print("Using brute force:")
    print("Minimum distance:", min_distance_bf)
    print("Minimum path:", min_path_bf)

    # Print the result branch and bound
    print("Using branch and bound:")
    print("Minimum distance:", min_distance_bb)
    print("Minimum path:", min_path_bb)

    # Print the result nearest neighbor
    print("Using nearest neighbor:")
    print("Minimum distance:", min_distance_nn)
    print("Minimum path:", min_path_nn)

    


if __name__ == '__main__':
    main()