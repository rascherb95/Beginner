foundrange = []
print('How long is the list?')
x = int(input(''))

def rangefinder(number):

    n = 0
    while n < number:
        x = int(input('Add this to the list: \t'))
        foundrange.append(x)
        n += 1

def ListAverage(listname):
    a = sum(listname)
    b = len(listname)
    return a / b



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
print("Here's the average of the list")
print(ListAverage(foundrange))

print('There are',len(foundrange), 'numbers in the list')

input1 = int(input('Pick a # from the sorted list to remove:>\t'))

input1_list = foundrange[input1]
print(input1_list)
