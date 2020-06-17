import time

bottles = int(input("how many bottles do you see? "))

while bottles > 1:

    print(bottles, 'bottles of beer on the wall')
    time.sleep(.75)
    print(bottles, 'bottles of beer')
    time.sleep(.75)
    print('take one down')
    time.sleep(.75)
    print('pass it around')
    bottles = bottles - 1
    time.sleep(.75)
    if bottles >1:
        print(bottles, 'bottles of beer on the wall')
    else:
        print(bottles, 'bottle of beer on the wall')
    print('-'*25)
    time.sleep(1)

if bottles == 1:
    print(bottles, 'bottle of beer on the wall')
    time.sleep(.75)
    print(bottles, 'bottle of beer')
    time.sleep(.75)
    print('take one down')
    time.sleep(.75)
    print('pass it around')
    bottles = bottles - 1
    time.sleep(.75)
    print('no more bottles of beer on the wall')
    time.sleep(.75)
    print('-'*25)
    time.sleep(.75)
    print("\nDamn, you're all out of beer!\n")
