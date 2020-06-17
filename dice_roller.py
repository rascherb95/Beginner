import random
import time

roll_again = 'yes'

print('\nWelcome to the dice roller\n')
time.sleep(1)

print('\nLet\'s begin\n')
time.sleep(1)

while roll_again == 'yes' or roll_again == 'y':
    print('\nRolling the dice...\n')
    time.sleep(1)
    player1 = random.randint(1,6)
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
