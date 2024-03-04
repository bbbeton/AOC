from aoc7 import get_numbers, get_win_numbers

with open('aoc7-8.txt') as file_input:

    file = file_input.read().splitlines()

cards = []

for i in range(len(file)):
    cards.append(int(1))

#print(cards)

for i in range(len(file)):
    score = 0
    score_curr = 0
    your_numbers = get_numbers(file[i])
    winning_numbers = get_win_numbers(file[i])
    for number in your_numbers:
        for win_number in winning_numbers:
            if number == win_number:
                # print (f'{number} is {win_number}!')
                score_curr += 1
                break
    if score_curr != 0:
        score += 1
        if score_curr < len(file):
            for k in range(score_curr):
                cards[i+1+k] += cards[i]
        # print(score_curr)
        # print(cards)

print(sum(cards))

