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

def find_length(distances, city, cities):
    current_city = city
    visited_cities = []
    route_length = 0
    while not len(visited_cities) == len(cities):
        for distance in distances:
            if current_city in distance[0] and current_city not in visited_cities:
                visited_cities.append(current_city)
                if current_city == distance[0][1]:
                    current_city = distance[0][0]
                else:
                    current_city = distance[0][1]
                if current_city not in visited_cities:
                    route_length += distance[1]
    return(route_length)

# def find_length(distances, city, cities):
#     current_city = city
#     visited_cities = []
#     route_length = 0
#     while len(visited_cities) < len(cities):
#         shortest_route = float('inf')
#         for distance in distances:
#             if current_city in distance[0] and current_city not in visited_cities:
#                 if distance[1] < shortest_route and shortest_route != 0:
#                     shortest_route = distance[1]
#                     if current_city == distance[0][1]:
#                         next_city = distance[0][0]
#                     else:
#                         next_city = distance[0][1]
#         visited_cities.append(current_city)
#         current_city = next_city
#         route_length += shortest_route
                
#     return(route_length)

if __name__ == '__main__':
    distances = []
    routes = []
    for line in file:
        distances.append(read_distances(line))
    starting_cities = get_cities(distances)
    for city in starting_cities:
        routes.append(find_length(distances, city, starting_cities))
    print(routes)
