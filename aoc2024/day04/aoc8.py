with open("aoc7-8.txt") as file_input:
    file = file_input.read().splitlines()

def find_xmas(text_file):
    keywords = {'MAS', 'SAM'}
    xmas_number = 0
    for i in range(1, len(text_file) - 1):
        for j in range(1, len(text_file[i]) - 1):
            if text_file[i][j] == 'A':
                checked_word1 = ''
                checked_word2 = ''
                for k in range(3):
                    checked_word1 += text_file[i-1+k][j-1+k]
                    checked_word2 += text_file[i+1-k][j-1+k]
                if checked_word1 in keywords and checked_word2 in keywords:
                    xmas_number += 1
    return xmas_number

if __name__ == "__main__":
    print(find_xmas(file))