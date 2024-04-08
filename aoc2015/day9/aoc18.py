from itertools import permutations
from aoc17 import read_distances, get_cities, get_length

with open('aoc17-18.txt') as file_input:
    file = file_input.read().splitlines()

if __name__ == '__main__':
    distances = []
    routes = []
    for line in file:
        distances.append(read_distances(line))
    starting_cities = get_cities(distances)
    print(starting_cities)
    possible_routes = permutations(starting_cities)
    for route in list(possible_routes):
        routes.append(get_length(route, distances))
    print(max(routes))
    # print(routes)
