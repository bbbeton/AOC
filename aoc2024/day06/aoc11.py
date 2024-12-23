with open('aoc11-12.txt') as file_input:
    file = file_input.read().splitlines()

def find_guard(text_file):
    column = 0
    row = 0
    for i in range(len(text_file)):
        for j in range(len(text_file[i])):
            if text_file[i][j] == '^':
                column = j
                row = i
                break
        if column == j and row == i:
            break
    return row, column 

if __name__ == "__main__":
    print(find_guard(file))
