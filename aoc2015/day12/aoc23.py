#initial try - check why doesn't work

# with open('aoc23-24.txt') as file_input:
#     file = file_input.read().splitlines()

# def get_sum(input):
#     number = ''
#     numbers = []
#     for i in range(len(input)):
#         if input[i].isdigit():
#             start = i
#             number += input[i]
#             if not input[i+1].isdigit() or i == len(input) - 1:
#                 if input[start-1] == '-':
#                     numbers.append(-int(number))
#                     number = ''
#                 else:
#                     numbers.append(int(number))
#                     number = ''
#     return sum(numbers)

# if __name__ == "__main__":
#     print(get_sum(file[0]))
            

import json

with open('aoc23-24.txt') as file_input:
    content = file_input.read()

def get_sum(data):
    numbers = []

    def extract_numbers(obj):
        if isinstance(obj, int):
            numbers.append(obj)
        elif isinstance(obj, list):
            for item in obj:
                extract_numbers(item)
        elif isinstance(obj, dict):
            for value in obj.values():
                extract_numbers(value)

    extract_numbers(json.loads(data))
    return sum(numbers)

if __name__ == "__main__":
    print(get_sum(content))
               
