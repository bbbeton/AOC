from aoc17 import get_sequence

with open('aoc17-18.txt') as file_input:
    file = file_input.read().splitlines()

def predict_number(list):
    for i in range(1,len(list)):
        list[-i-1].insert(0,list[-i-1][0] - list[-i][0])
    return list[0][0]

if __name__ == "__main__":
    score = 0
    for i in range(len(file)):
        sequence = [int(num) for num in file[i].split()]
        sequences = [sequence]
        get_sequences = True
        while get_sequences:
            sequence = get_sequence(sequence)
            sequences.append(sequence)
            if all(element == 0 for element in sequence):
                get_sequences = False
        score += predict_number(sequences)
        #print(sequences)
    print(score)