with open("aoc23-24.txt") as file_input:
    file = file_input.read().splitlines()

springs = []
numbers = []

for line in file:
    springs.append(line.split()[0])
    numbers.append(line.split()[1].split(','))
i=0
for spring in springs:
    print(spring)
    print(numbers[i])
    i += 1