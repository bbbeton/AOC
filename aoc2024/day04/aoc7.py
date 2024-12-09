with open("aoc7-8.txt") as file_input:
    file = file_input.read().splitlines()

def countLine(text_file):
    xmas_number = 0
    for line in text_file:
        xmas_number += line.count('XMAS') + line.count('SAMX') 
    return xmas_number

def countDiagonal(textFile):
    diagonal_words = 0
    keywords = {'XMAS', 'SAMX'}
    for i in range(len(textFile)):
        for j in range(len(textFile[i])):
            if textFile[i][j] in {'S', 'X'} and i < len(textFile) - 3:
                if len(textFile[i]) - 3 > j > 2:
                    checked_word1 = ''
                    checked_word2 = ''
                    for k in range(4):
                        checked_word1 += textFile[i+k][j+k]
                        checked_word2 += textFile[i+k][j-k]
                    if checked_word1 in keywords:
                        diagonal_words += 1
                    if checked_word2 in keywords:
                        diagonal_words += 1
                elif j <= 2:
                    checked_word1 = ''
                    for k in range(4):
                        checked_word1 += textFile[i+k][j+k]
                    if checked_word1 in keywords:
                        diagonal_words += 1
                elif j >= len(textFile) - 3:
                    checked_word1 = ''
                    for k in range(4):
                        checked_word1 += textFile[i+k][j-k]
                    if checked_word1 in keywords:
                        diagonal_words += 1
    return diagonal_words

def countVertical(textFile):
    vertical_words = 0
    keywords = {'XMAS', 'SAMX'}
    for i in range(len(textFile)):
        for j in range(len(textFile[i])):
            if textFile[i][j] in {'S', 'X'} and i < len(textFile) - 3:
                checked_word = ''
                for k in range(4):
                    checked_word += textFile[i+k][j]
                if checked_word in keywords:
                    vertical_words += 1
    return vertical_words

if __name__ == "__main__":
    xmas = countVertical(file) + countDiagonal(file) + countLine(file)
    print(xmas)
    print(countVertical(file))
    print(countLine(file))
    print(countDiagonal(file))