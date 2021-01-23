print('Hi stranger!')

#global variable
place = input('Where are you from motherfucker?')

def main():
    #local variable
    gender = 'female'

    if place != 'LA':
        print('Wrong answer' + gender)
    else:
        print('Whats up yo?')

main()