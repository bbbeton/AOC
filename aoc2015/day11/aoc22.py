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

def check_straight(password):
    for i in range(len(password) - 2):
        if (ord(password[i+1]) == ord(password[i]) + 1) and (ord(password[i+2]) == ord(password[i]) + 2):
            return True
    return False

def check_pairs(password):
    counter = 0
    used_letter = ''
    for i in range(len(password)-1):
        if password[i] == password[i+1] and counter == 0:
            used_letter = password[i]
            counter = 1
        if password[i] == password[i+1] and counter == 1 and password[i] != used_letter:
            return True
    return False
        
if __name__ == "__main__":
    while not check_pairs(pswd) or not check_straight(pswd):
        pswd = change_password(pswd)
    pswd = change_password(pswd)
    while not check_pairs(pswd) or not check_straight(pswd):
        pswd = change_password(pswd)
    print(''.join(pswd))