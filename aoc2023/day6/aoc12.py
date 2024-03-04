with open('aoc11-12.txt') as file_input:
    file = file_input.read().splitlines()

def get_nums(line):
    numbers = ''
    for i in range(len(line)):
        numbers += line[i]
        if line[i] == ':':
            numbers = ''
    seed = int(numbers.replace(' ',''))
    return seed

time = get_nums(file[0])
distance = get_nums(file[1])
record = 0

for j in range(time):
        distance_time = (time-j)*j
        if distance_time > int(distance):
            record += 1
        if distance_time < int(distance) and record != 0:
             break

print(record)