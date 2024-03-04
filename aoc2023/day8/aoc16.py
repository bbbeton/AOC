from aoc15 import get_directions, get_routes

with open('aoc15-16.txt') as file_input:
    file = file_input.read().splitlines()

        
def get_z_route(routes, node, directions):
    steps = 0
    while node[2] != 'Z':
        for i in range(len(directions)):
            for j in range(len(routes)):
                if routes[j][0] == node:
                    if directions[i] == 'L':
                        node = routes[j][1]
                        steps += 1
                        break
                    elif directions[i] == 'R':
                        node = routes[j][2]
                        steps += 1
                        break       
            if node[2] == 'Z':
                break
    return(steps)

if __name__ == "__main__":
    directions = get_directions(file)
    routes = get_routes(file)
    node = 'AAA'

    nodes = []

    for i in range(len(routes)):
        if routes[i][0][2] == 'A':
            nodes.append(routes[i][0])
            print(routes[i][0])

    print(nodes)

    routes = []

    for i in range(len(nodes)):
        routes.append(get_z_route(routes, nodes[i], directions))
        print(routes[i])
    
        
    print(routes)