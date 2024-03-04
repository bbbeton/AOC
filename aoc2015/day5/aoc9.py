def check_vowels(char):
    vowels = 'aeiou'
    counter = 0
    for vowel in vowels:
        if vowel in char:
            counter += char.count(vowel)
    if counter > 2:
        return True
    return False

def check_neighbours(char):
    for i in range(len(char)-1):
        if char[i] == char[i+1]:
            return True
    return False  

def check_strings(char):
    strings = ['ab', 'cd', 'pq', 'xy']
    for string in strings:
        if string in char:
            return False
    return True

count_nice = 0
with open('aoc9-10.txt') as file_input:
    for line in file_input:
        if check_vowels(line) and check_neighbours(line) and check_strings(line):
            count_nice += 1
            print(f"{line} is nice!")
        else:
            print(f"{line} is naughty!")

print(count_nice)

