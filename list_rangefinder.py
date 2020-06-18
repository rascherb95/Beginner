foundrange = []
print('How long is the list?')
x = int(input(''))

def rangefinder(number):

    n = 0
    while n < number:
        x = int(input('Add this to the list: \t'))
        foundrange.append(x)
        n += 1

rangefinder(x)
foundrange.sort()
print(*foundrange)

forgetful = input('Did you forget any? \n y/n: \t')

if forgetful == 'y' or forgetful == 'yes':
    print('How many did you forget?')
    forgotten = int(input(''))
else:
    print('Nice memory!')

def rangefinder_add(number):

    n = 0
    while n < number:
        x = int(input('Type the ones you\' forgotten'))
        foundrange.append(x)
        n += 1

rangefinder(forgotten)
foundrange.sort()
print("Here's the updated list")
print(*foundrange)


list1 = foundrange[0]
print("Here's the first number in the list")
print(list1)


input1 = int(input('Pick a # from the sorted list:>\t'))

input1_list = foundrange[input1]
print(input1_list)
