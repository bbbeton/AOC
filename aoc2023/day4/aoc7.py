def get_numbers(char):
    number = ''
    for i in range(len(char)):
        number += char[i]
        if char[i] == ':':
            number = ''
        if char[i] == '|':
            break
    liczby = list(filter(None, number.replace('|','').split()))
    return liczby

def get_win_numbers(char):
    number = ''
    for i in range(len(char)):
        number += char[i]
        if char[i] == '|':
            number = ''
        if char[i] == '\n':
            break
    liczby = list(filter(None, number.replace('\n','').split()))
    return liczby

if __name__ == '__main__':
    with open('aoc7-8.txt') as file_input:
        score = 0
        cards = []
        for line in file_input:    
            score_curr = 0
            your_numbers = get_numbers(line)
            winning_numbers = get_win_numbers(line)
            # print(your_numbers)
            # print(winning_numbers)
            for number in your_numbers:
                for win_number in winning_numbers:
                    if number == win_number:
                        # print (f'{number} is {win_number}!')
                        score_curr += 1
                        break
            if score_curr != 0:
                score += 2**(score_curr-1)
    
    print(f"Suma = {score}")