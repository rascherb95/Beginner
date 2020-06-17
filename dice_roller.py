import random
import time

start_game = input('\n Do you want to play "Dice Roller?\n \t y/n>')

if start_game == 'y':
    roll_again = 'yes'
    print("Enjoy!")
else:
    time.sleep(2)
    print('\n\nfuck you too buddy\n\n')
    quit()

print('\nWelcome to the dice roller\n')
time.sleep(1)

print('\nLet\'s begin\n') #\' used on purpose to test
time.sleep(1)

while roll_again == 'yes' or roll_again == 'y':
    print('\nRolling the dice...\n')
    time.sleep(1)
    player1 = random.randint(1,6)  #to eventually add variable dice #'s
    enemy = random.randint(1,6)

    print('You rolled a:', f'{player1}')
    time.sleep(1)
    print('Now for the enemy...')
    time.sleep(1)
    print('The enemy rolled a', f'{enemy}')
    time.sleep(1.25)
    if player1 > enemy:
        print('\nCongrats, you won!')
    elif player1 == enemy:
        print('\nYou tied')
    else:
        print('\nYou lose')
    time.sleep(1.5)
    roll_again = input('\nDo you want to roll again? >')

if roll_again != 'yes' or roll_again != 'y':
    print("\nThanks for playing!\n")
