#initial try

with open('aoc23-24.txt') as file_input:
    file = file_input.read().splitlines()

def get_sum(input):
    number = ''
    numbers = []
    for i in range(len(input)):
        if input[i].isdigit():
            if not input[i-1].isdigit() and i > 0:
                start = i
            number += input[i]
            if not input[i+1].isdigit() or i == len(input) - 1:
                if input[start-1] == '-':
                    numbers.append(-int(number))
                    number = ''
                else:
                    numbers.append(int(number))
                    number = ''
    return sum(numbers)

if __name__ == "__main__":
    print(get_sum(file[0]))