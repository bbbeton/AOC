import hashlib

puzzle_input = 'yzbqklnj'

def make_md5(char):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    # Update the hash object with the input string
    md5_hash.update(char.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    hex_representation = md5_hash.hexdigest()
    return hex_representation

add_value = 0
hex_output = make_md5(puzzle_input+str(add_value))

while str(hex_output)[:5] != '00000':
    add_value += 1
    hex_output = make_md5(puzzle_input+str(add_value))

print(add_value)
