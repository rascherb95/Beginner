import random
import time

start_game = input('''\nWould you like to play "Number Guesser?"\n\t\ty/n >\t''')

if start_game == 'y':
    print('Good choice!')       #allow user specify play or nah
else:
    quit()

print('Welcome to the Number Guesser!')

time.sleep(1)

print('Select two numbers')

time.sleep(1)

num1, num2 = int(input('#1: ')),int(input('#2: ')) #integer checks

time.sleep(1)

lower_bound = min(num1,num2)
upper_bound = max(num1,num2)

correct_answer = (random.randint(lower_bound, upper_bound))

print('Your numbers are:', lower_bound,'and',upper_bound)

time.sleep(1)

print('How many guesses would you like?')

lives = int(input('Select a number of lives:\n\t'))

time.sleep(1)

print("You'll start with", lives, 'lives')

guesses_taken = 0

while guesses_taken < lives:
    print('What do you think the answer is?')
    guess = int(input()) #add integer checks
    if guess == correct_answer:
        print('Congrats! You won!')
        quit()
    #elif:
    #    pass
    else:
        guesses_taken += 1
        print('Ha! Try again')
        time.sleep(1)

if guesses_taken == lives:
    print('Sorry, you ran out of lives!')
    quit()



    #quit()
