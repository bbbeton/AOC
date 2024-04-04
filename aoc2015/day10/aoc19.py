def count_numbers(number):
    output_number = ''
    numbers_count = 0
    for i in range(len(number)):
        numbers_count += 1
        if i < len(number) - 1:
            if number[i] != number[i+1]:
                output_number += str(numbers_count) + number[i]
                numbers_count = 0
        else:
            output_number += str(numbers_count) + number[i]
    return output_number

if __name__ == "__main__":
    i = 0
    number = "1113222113"
    while i < 40:
        number = count_numbers(number)
        i += 1
    print(len(number))
        

