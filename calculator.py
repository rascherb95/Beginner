def menu():
    """load the calculator menu"""
    print('\n\nWelcome to the calculator')
    print('Here are your options\n')
    print('1) Addition')
    print('2) Subtraction')
    print('3) Division')
    print('4) Multiplication')
    print('5) Square-ing')
    print('  Exit Calculator\n')
    int(input('What would you like to do?\n\t>'))

def add(a,b):
    z = a + b
    print('A + B is:', z)

def subtract(a,b):
    z = a - b
    print('A - B is:', z)

def divide(a,b):
    z = a / b
    print('A / B is:', z)

def multiply(a,b):
    z = a * b
    print('A * B is:', z)

def square(a,b):
    z = a ** b
    print('A to the B power is:', z)

run = True

while run == True:
    print('What would you like to do?')
    choice = menu()
    if choice == 1:
        add(input(x,y).split(separator, maxsplit))
        print(choice)
    else:
        run = False
        break
