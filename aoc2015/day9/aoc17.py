from itertools import permutations

with open('aoc17-18.txt') as file_input:
    file = file_input.read().splitlines()
    
def read_distances(string):
    distances = string.split(' = ')
    distances[0] = distances[0].split(' to ')
    distances[1] = int(distances[1])
    return distances
    
def get_cities(distances):
    cities = []
    for distance in distances:
        if distance[0][0] not in cities:
            cities.append(distance[0][0])
        if distance[0][1] not in cities:
            cities.append(distance[0][1])
    return cities

def get_length(route, distances):
    total_distance = 0
    for i in range(1, len(route)):
        for j in range(len(distances)):
            if route[i] in distances[j][0] and route[i-1] in distances[j][0]:
                total_distance += int(distances[j][1])
                break
    return total_distance


if __name__ == '__main__':
    distances = []
    routes = []
    for line in file:
        distances.append(read_distances(line))
    starting_cities = get_cities(distances)
    #print(starting_cities)
    possible_routes = permutations(starting_cities)
    for route in list(possible_routes):
        routes.append(get_length(route, distances))
    print(min(routes))
    # print(routes)