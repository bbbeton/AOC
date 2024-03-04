with open('aoc17-18.txt') as file_input:
    file = file_input.read().splitlines()

def get_sequence(char):
    new_sequence = []
    for i in range(len(char)-1):
        new_sequence.append(int(char[i+1])- int(char[i]))
    return new_sequence

def predict_number(list):
    for i in range(1,len(list)):
        list[-i-1].append(list[-i][-1] + list[-i-1][-1])
    return list[0][-1]

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

