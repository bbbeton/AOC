with open('aoc11-12.txt') as file_input:
    file = file_input.read().splitlines()

def get_nums(line):
    numbers = ''
    for i in range(len(line)):
        numbers += line[i]
        if line[i] == ':':
            numbers = ''
    seeds = numbers.split()
    return seeds

times = get_nums(file[0])

distances = get_nums(file[1])

records = []

for i in range(len(times)):
    time = int(times[i])
    record = 0
    for j in range(time):
        speed = j
        distance = (time-j)*speed
        #check if the record is beaten
        if distance > int(distances[i]):
            record += 1
    records.append(record)
    
#get the multiplication
number = records[0]

for i in range(1, len(records)):
    number *= records[i]

print(number)
