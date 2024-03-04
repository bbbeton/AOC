with open('aoc13-14.txt') as file_input:
    file = file_input.read().splitlines()

def get_hand(char):
    hand = char.split()
    hand[0] = str(hand[0])
    hand[1] = int(hand[1])
    return hand

hands = []
ranked_cards = 'A K Q T 9 8 7 6 5 4 3 2 J'.split()
print(ranked_cards)

def get_type(hand, ranked):
    count1 = 0
    count2 = 0
    for rank in ranked:
        count = hand.count(rank)
        if count1 == 0 and count >1:
            count1 = count
        elif count1 != 0 and count > 1:
            count2 = count
    
    if count1 == 5:
        score = 7
    elif count1 == 4:
        if hand.count('J') == 1 or hand.count('J') == 4:
            score = 7
        else:
            score = 6
    elif (count1 == 3 and count2 == 2) or (count2 == 3 and count1 == 2):
        if hand.count('J') == 2 or hand.count('J') == 3:
            score = 7
        else:
            score = 5
    elif count1 == 3:
        if hand.count('J') == 3:
            score = 6
        elif hand.count('J') == 2:
            score = 7
        elif hand.count('J') == 1:
            score = 6
        else:
            score = 4
    elif count1 == 2 and count2 == 2:
        if hand.count('J') == 2:
            score = 6
        elif hand.count('J') == 1:
            score = 5
        else:
            score = 3
    elif count1 == 2:
        if hand.count('J') == 2:
                score = 4
        elif hand.count('J') == 1:
            score = 4
        else:
            score = 2
    else:
        if hand.count('J') == 1:
            score = 2
        else:
            score = 1
    
    return score
    
five = []
four = []
full = []
three = []
pairs = []
pair = []
high_card = []

for i in range(0,len(file)):
    hands.append(get_hand(file[i]))
    hands[i].append(get_type(hands[i][0], ranked_cards))
    if hands[i][-1] == 7:
        five.append(hands[i][0])
    elif hands[i][-1] == 6:
        four.append(hands[i][0])
    elif hands[i][-1] == 5:
        full.append(hands[i][0])
    elif hands[i][-1] == 4:
        three.append(hands[i][0])
    elif hands[i][-1] == 3:
        pairs.append(hands[i][0])
    elif hands[i][-1] == 2:
        pair.append(hands[i][0])
    else:
        high_card.append(hands[i][0])
    print(hands[i])
rank = 1

high_card.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)
pair.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)
pairs.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)
three.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)
full.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)
four.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)
five.sort(key = lambda x :[ranked_cards.index(char) for char in x], reverse = True)



print(f"{five}\n{four}\n{full}\n{three}\n{pairs}\n{pair}\n{high_card}")


rank = 0
win = 0

for hand in high_card:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")
            

for hand in pair:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")
            

for hand in pairs:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")

for hand in three:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")


for hand in full:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")
   

for hand in four:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")
    
for hand in five:
    for i in range(len(hands)):
        if hand == hands[i][0]:
            rank += 1
            win += rank*hands[i][1]
            print(f"{hand} - hand\n{rank} - rank\n{hands[i][1]} - bet\n\n")
    

print(win)