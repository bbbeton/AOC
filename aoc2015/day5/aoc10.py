with open('aoc9-10.txt') as file_input:
    file = file_input.read().splitlines()

def check_letter(char):
    for i in range(len(char)-2):
        if char[i] == char[i+2]:
            return True
    return False

def check_pairs(char):
    for i in range(len(char)-1):
        pair =  char[i] + char[i+1]
        if char.count(pair) >= 2:
            return True
    return False

if __name__ == "__main__":
    nice = 0
    for j in range(len(file)):
        letter = check_letter(file[j])
        pair = check_pairs(file[j])
        if letter and pair:
            nice += 1
    print(nice)