with open('aoc15-16.txt') as file_input:
    file = file_input.read().splitlines()

def get_directions(char):
    directions = ''
    for i in range(len(char)):
        if char[i]:
            directions += char[i]
        else: 
            break
    return directions

def get_routes(char):
    routes = []
    for i in range(len(char)):
        if not char[i]:
            start = i+1
            break
    for i in range(start,len(char)):
        route = ''.join(n for n in char[i] if n.isalpha() or n == ',' or n =='=').replace('=',',').split(',')
        routes.append(route)
    return routes
        

directions = get_directions(file)
routes = get_routes(file)


nodes = []
for i in range(len(routes)):
    if routes[i][0][2] == 'A':
        nodes.append(routes[i][0])
        print(routes[i][0])

steps_all = []
for k in range(len(nodes)):
    node = nodes[k]
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
    steps_all.append(steps)
    print(steps)
    
print(steps_all)

#answer = najmniejsza wspolna wielokrotnosc