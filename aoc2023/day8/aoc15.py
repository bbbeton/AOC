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
        
if __name__=="__main__":
    directions = get_directions(file)
    routes = get_routes(file)
    node = 'AAA'
    steps = 0

    while node != 'ZZZ':
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
            if node == 'ZZZ':
                break
        
    print(steps)