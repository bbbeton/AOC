import json

with open('aoc23-24.txt') as file_input:
    content = file_input.read()

def get_sum(data):
    numbers = []

    def extract_numbers(obj):
        if isinstance(obj, int):
            numbers.append(obj)
        elif isinstance(obj, list):
            if "red" not in obj:
                for item in obj:
                    extract_numbers(item)
        elif isinstance(obj, dict):
            if "red" not in obj.values():
                for value in obj.values():
                    extract_numbers(value)

    extract_numbers(json.loads(data))
    return sum(numbers)

if __name__ == "__main__":
    print(get_sum(content))