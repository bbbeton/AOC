with open('aoc17-18.txt') as file_input:
    file = file_input.read().splitlines()
    
def read_distances(string):
    distances = string.split(' = ')
    distances[0] = distances[0].split(' to ')
    return distances
    
def get_cities(distances):
    cities = []
    for distance in distances:
        if distance[0][0] not in cities:
            cities.append(distance[0][0])
        if distance[0][1] not in cities:
            cities.append(distance[0][1])
    return cities


if __name__ == '__main__':
    distances = []
    for line in file:
        distances.append(read_distances(line))
    print(get_cities(distances))