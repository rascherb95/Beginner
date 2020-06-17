import random
import time

start_game = input('''\nWould you like to play "Number Guesser?"\n\t\ty/n >\t''')

if start_game == 'y':
    game_on = 'YES'
    print("Good luck!")
else:
    game_on == 'NO'
    quit()

print('Welcome to the Number Guesser!')

time.sleep(1)

#print('Select two numbers, separated by a comma')

time.sleep(1)

NG_range = []
maxLengthList = 2

while len(NG_range) < maxLengthList:
    number = int(input("Select a number\n >\t"))  #error check for no number?
    NG_range.append(number)

NG_range.sort(key=int)   #sorts the list, only works with integer input

print('You have selected the following numbers:')
print(f'\t{NG_range}')

time.sleep(1)

print('Great! Now let\'s play')
time.sleep (1)

ready_check = input('Are you ready?\n y/n >\t')

if ready_check == 'y':
    pass

else:
    time.sleep(1)
    print('Come back later!')
    quit()
