import random
import time
import sys

start_game = input('''\nWould you like to play "Number Guesser?"\n\t\ty/n >\t''')

if start_game == 'y':
    print('Good choice!')       #allow user specify play or nah
else:
    print('See you later!')
    sys.exit()

print('Welcome to the Number Guesser!')

time.sleep(1)

print('Select two numbers')

time.sleep(1)

while True:
    try:
        num1 = int(input('Number #1 > \t'))
        break
    except:
        ValueError
        print('Please type a number')

while True:
    try:
        num2 = int(input('Number #2 > \t'))
        break
    except:
        ValueError
        print('Please type a number')


time.sleep(1)

lower_bound = min(num1,num2)
upper_bound = max(num1,num2)

correct_answer = (random.randint(lower_bound, upper_bound))

print('Your numbers are:', lower_bound,'and',upper_bound)

time.sleep(1)

print('How many guesses would you like?')

while True:
    try:
        lives = int(input('> \t'))
        break
    except:
        ValueError
        print('Please type a number')

time.sleep(1)

if lives > 0:

    print("You'll start with", lives, 'lives')

else:

    print("So you dont want to play")

time.sleep(1)

#    print('See you later!')

time.sleep(1)


#line 68 is only there to set a lives_left val, as setting it = 0 breaks code
#playerwin is changed by the nested ifs in the while loop
#guessses+taken isnt
#workaround is using lives_left -=1 instead of guesses_taken += 1

#i believe it is bpecause (=0) is immutable and would require a (guesses_taken =)
#similar to playerwin, lives_left = (mutable - mutable) so -= works

guesses_taken = 0    #are vars (set = X) immutable, like below var playerwin
lives_left = lives - guesses_taken   #doesn't run without vars. cant set = 0
playerwin = False



while lives_left > 0 :
    if lives_left == 1: #correctly runs
        print('Last life! Make it count')
        while True:
            try:
                guess = int(input('> \t'))
                if guess == correct_answer:
                    playerwin = True
                    print(playerwin)
                else:
                    print('Wrong 1!')
                    lives_left -= 1
                    print(playerwin)
                break
            except:
                ValueError
                print('Please guess a number 1')

    else: #correctly runs
        time.sleep(.5)
        print(f'You have {lives_left} lives remaining') #correctly prints
        print('What\'s my number?')
        while True:

            try:
                guess = int(input('> \t'))
                if guess == correct_answer:
                    playerwin = True
                    print(playerwin)

                else:
                    print('Wrong!')
                    lives_left -= 1    #this operates correctly
                    guesses_taken += 1 #this doesnt do shit
                    print(playerwin)

                break

            except:
                ValueError
                print('Please type a number')


    if lives_left == 0: #correctly runs except for starting with 0 lives
        print('Sorry, you ran out of lives!')
        sys.exit()

if (playerwin):   #win 1 & win2 conditions properly work
    print('Win 1')
else:
    print('you lose')
    sys.exit()

    #quit()
