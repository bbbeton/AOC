from aoc21_22 import alphabet, pswd, illegal_chars

def change_password(password):
    for i in range(1, len(password)):
        if password[-i] != 'z':
            if chr(ord(password[-i]) + 1) in illegal_chars:
                password[-i] = chr(ord(password[-i]) + 2)
                for j in range(1, i-1):
                    password[-i+j] = 'a'
                break
            else:
                password[-i] = chr(ord(password[-i]) + 1) 
                break
        else:
            password[-i] = 'a'       
    return password

while pswd[3] != 'q':
    pswd = change_password(pswd)
print(pswd)

