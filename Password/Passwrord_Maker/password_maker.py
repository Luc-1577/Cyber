import random as rd

def peak(x, y):
    return chr(rd.randint(x, y))

def interwine(x, R2):
    x = list(x)
    rd.shuffle(x)
    
    while len(x) > R2:
        y = x.pop()

    password = ''.join(x)
    return password

def uppercase(R2):
    password = ''
    while len(password) < R2:
        char = peak(65, 90)
        password += char
    return password

def lowercase(R2):
    password = ''
    while len(password) < R2:
        char = peak(97, 122)
        password += char
    return password

def pin(R2):
    password = ''
    while len(password) < R2:
        char = peak(48, 57)
        password += char
    return password

def symbols(R2):
    password = ''
    while len(password) < R2:
        char = peak(33, 47)
        password += char
    return password    

def anything(R2):
    password = ''
    while len(password) < R2:
        char = peak(32, 125)
        password += char
    return password
    

    
print('0 - Stop',
      '1 - Uppercase only',
      '2 - Lowercase only',
      '3 - Pin',
      '4 - Symbols',
      
      '5 - Uppercase & Lowercase',
      '6 - Uppercase & Numbers',
      '7 - Uppercase & Symbols',

      '8 - Lowercase & Numbers',
      '9 - Lowercase & Symbols',

      '10 - Numbers & Symbols',

      '11 - Uppercase & Lowercase & Numbers',
      '12 - Uppercase & Lowercase & Symbols',
      '13 - Uppercase & Numbers & Symbols',

      '14 - Lowercase & Numbers & Symbols',
      
      '15 - Random',

      '16 - All',

      '17 - Customized password \n'
      
      ,sep='\n')

while True:
    R1 = input('Choose an option > ')
    R1 = R1.strip()
    if not R1.isdigit() or int(R1) > 17:
        print('Error \n')
        break
    
    R2 = input('Password length (min. 4) > ')
    R2 = R2.strip()
    if not R2.isdigit():
        print('Error \n')
        break
    R2 = int(R2)
    while R2 < 4:
        R2 += 1

    match R1:
        case '0':
            break
        
        case '1':
            password = uppercase(R2)
            print(f'\nYour password: {password} \n\n')

        case '2':
            password = lowercase(R2)
            print(f'\nYour password: {password} \n\n')

        case '3':
            password = pin(R2)
            print(f'\nYour password: {password} \n\n')

        case '4':
            password = symbols(R2)
            print(f'\nYour password: {password} \n\n')

        case '5':
            password = interwine(uppercase(R2) + lowercase(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '6':
            password = interwine(uppercase(R2) + pin(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '7':
            password = interwine(uppercase(R2) + symbols(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '8':
            password = interwine(lowercase(R2) + pin(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '9':
            password = interwine(lowercase(R2) + symbols(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '10':
            password = interwine(pin(R2) + symbols(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '11':
            password = interwine(uppercase(R2) + lowercase(R2) + pin(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '12':
            password = interwine(uppercase(R2) + lowercase(R2) + symbols(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '13':
            password = interwine(uppercase(R2) + pin(R2) + symbols(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '14':
            password = interwine(lowercase(R2) + pin(R2) + symbols(R2), R2)
            print(f'\nYour password: {password} \n\n')

        case '15':
            password = anything(R2)
            print(f'\nYour password: {password} \n\n')

        case '16':
            divisible = R2
            if divisible & 1:
                divisible += 1
            password = interwine(uppercase(divisible/4) + lowercase(divisible/4) + pin(divisible/4) + symbols(divisible/4), R2)
            print(f'\nYour password: {password} \n\n')

        case '17':
            cusmtom = input('Add a password prefix > ')
            divisible = R2
            if divisible & 1:
                divisible += 1
            password = cusmtom + interwine(pin(divisible/4) + symbols(divisible/4), R2)
            print(f'\nYour password: {password} \n\n')