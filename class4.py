def oneWayIf(myArg):
    'revisiting a one way if statement'
    if myArg > 70:
        print('it is starting to feel like summer')


def twoWayIf(myArg):
    'revisiting a two way if statement'
    if myArg > 70:
        print('it is starting to feel like summer')
    else:
        print('it must not be summer yet')


def multiWayIf(myArg):
    'learning a multi way if statement'

    #the only way else gets triggered
    #is if myArg < 70 or >= 100
    if myArg > 70 and myArg < 75:
        print('it is starting to feel like summer')
    elif myArg >= 75 and myArg < 80:
        print('summer is coming')
    elif myArg >= 80 and myArg < 85:
        print('summer is here and it is glorious')
    elif myArg >= 85 and myArg < 100:
        print('summer is here and it is no longer glorious, just hot')
    else:
        print('it must not be summer yet')

    print('my function is continuing')

def BMI(weight, height):
    'prints BMI report'

    height = height**2
    weight = weight*703

    bmi = weight / height

    if bmi < 18.5:
        print('Underweight')
    elif bmi < 25:
        print('Normal')
    else: # bmi >= 25
        print('Overweight')

    return bmi, height, weight

def arithmetic(lst):
    '''return True if list lst contains an arithmetic sequence,
       False otherwise'''

    if len(lst) < 2: # a sequence of length < 2 is arithmetic
        return True

   # check that the difference between successive numbers is
   # equal to the difference between the first two numbers 
    diff = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        if lst[i+1] - lst[i] != diff:
            return False

    return True

def inBoth(lst1, lst2, lst3):
    retVal = []
    for i in lst1:
        for k in lst3:
            for j in lst2:
                if i == k and i != j:
                    continue
                elif i == j and i == k:
                    retVal.append(i)
                    break

            
    
    return retVal

def embeddedLists(lst):
    for item in lst:
        if type(item) is list:
            print('I\'m going to iterate over this list')
            print(item)
        else:
            print('This is not a list: {}'.format(item))

def embeddedListsWithErrors(lst):
    for item in lst:
        try:
            for i in item:
                print(i)
        except TypeError as tx:
            print(tx)
            print('This is not a list: {}'.format(item))
        except Exception as ex:
            print(ex)
            print('This is not a list: {}'.format(item))

def print2D(t):
    'prints values in 2D list t as a 2D table'
    for row in t:
        for item in row:
            print(item, end='\t')
        print()

def incr2D(t):
    'increments each number in 2D list t'
    print('Original List: {}'.format(t))
    for i in range(0,len(t)):
        row = t[i]
        for col in range(0,len(row)):
            t[i][col] += 1

    print('New list: {}'.format(t))

def incrStrings(t):
    'increments each number in 2D list t'
    retVal = []
    for i in range(0,len(t)):
        row = t[i]
        for j in range(i,len(t)):
            check = t[j]
            if row == check:
                continue
            for col in range(0,len(row)):            
                val2 = check[col]
                if val2 in row:
                    print(row)
                    print(t[i+1])

                    retVal.append(row+check)
    return retVal


def myWhile(counter):
    try:
        while counter < 1000:
            print(counter)
            

            if counter %2 == 0:
                counter += 3
                #skips the code underneath the continue statement
                #goes right back to the top of the while statement
                continue
            
            counter += 1

    except KeyboardInterrupt as k:
        print("You found yourself in an infinite loop.  HOORAY")
        print(k)

def gatherInput():
    userInput = ''
    # while userInput != 'q':
    #     print('Here is my menu')
    #     print('Press h for help')
    #     print('Press q to quit')
    #     userInput = input("Enter input: ")

    #     if userInput == 'h':
    #         print('Press q to quit')

    while True:
        shouldIBreak = False
        print('Here is my menu')
        print('Press h for help')
        print('Press q to quit')
        userInput = input("Enter input: ")

        if userInput == 'h':
            print('Press q to quit')
        elif userInput == 'q':
            break

        for c in userInput:
            print(c)
            if c == 'q':
                shouldIBreak = True
                break
        if shouldIBreak is True:
            break

def fibonacci(bound):
    'returns the smallest Fibonacci number greater than bound'
    previous = 1	        # previous Fibonacci number
    current = 1	        # current Fibonacci number
    while current <= bound:
        # current becomes previous, and new current is computed
        previous, current = current, previous+current
    return current

def dictionaries():
    employee = {
	'864-20-9753': ['Anna', 'Karenina'],
	'987-65-4321': ['Yu', 'Tsun'],
	'100-01-0010': ['Hans', 'Castorp']
    }

    partTimers = {}
    partTimers['bodonne3'] = ['Brian', 'O\'Donnell']
    
    myKeyValues = partTimers['bodonne3']

    print(myKeyValues)

    myKeyValues.append('1060 W. Addison')
    myKeyValues.append('We\'re on a mission from God')

    #inserting a duplicate key will overwrite the value
    partTimers['bodonne3'] = 'Hello LA LA LA'

    partTimers[1212] = ['bodonne3', 'Brian', '1060 W. Addison']

    for k in partTimers.keys():
        print(partTimers[k])

    for key,value in partTimers.items():
        print(key)
        print(value)

    days = {'Mo': 1, 'Tu': 2, 'Th': 5, 'W': 3}
    for k in days.keys():
        print(days[k])






multiWayIf(83)

#yourBMI = 0
#sampleWeight = int(input('Enter your weight: '))
#sampleHeight = int(input('Enter your height(in cm): '))
#yourBMI, sampleHeight, sampleWeight = BMI(sampleWeight, sampleHeight)
#print(yourBMI)

lst = [3, 6, 9, 12, 15, 18]
lst2 = [1,4,2,9,3,18]
lst3 = [18, 5, 3, 9]
arithmetic(lst)
inBoth(lst, lst2, lst3)

myList = [lst,5,7,lst2,'purple','happy',lst3]
embeddedLists(myList)
embeddedListsWithErrors(myList)

intTable = [[3, 5, 7, 9],
        [0, 2, 1, 6],
        [3, 8, 3, 1]]

incr2D(intTable)

strTable = [['Adam Sandler', 'Happy Gilmore', 'Billy Madison'], ['Mike Myers', 'Waynes World', 'Austin Powers'], ['Dana Carvey', 'Waynes World', 'Master of Disguise'], ['Chris Farley', 'Billy Madison', 'Tommy Boy']]
incrStrings(strTable)

myWhile(0)

#gatherInput()

#fibonacci(55)

dictionaries()



