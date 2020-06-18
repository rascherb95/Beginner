import random
import time

start_game = input('''\nWould you like to play "Number Guesser?"\n\t\ty/n >\t''')

if start_game == 'y':
    game_on = 'YES'

else:
    game_on == 'NO'
    quit()

print('Welcome to the Number Guesser!')

time.sleep(1)

print('Select two numbers')

time.sleep(1)

num1, num2 = input('#1: '),input('#2: ')

time.sleep(1)

lower_bound = min(num1,num2)
upper_bound = max(num1,num2)

correct_answer = (random.randint(lower_bound, upper_bound))

print(answer1)

print('Your numbers are:', lower_bound,'and',upper_bound)

time.sleep(1)

print('How many guesses would you like?')

lives = int(input('Select a number of lives:\n\t'))

time.sleep(1)

print("You'll start with", lives, 'lives')

guesses_taken = 0

while guesses_taken < lives:
    print('What do you think the answer is?')
    guess = int(input())
    if guess == correct_answer:
        print('Congrats! You won!')
        quit()
    else:
        gueese_taken += 1
        continue


    #quit()
