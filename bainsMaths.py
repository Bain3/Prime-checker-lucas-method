



'''
The lucas number generator:
ex.: lucasNumber(3) = 4 (fourth lucas number)
'''
def lucasNumber(count):
    # Setting initial values
    base = 2
    base2 = 1
    three = 0
    if count == 0:  #Send 1 if count is zero
        return base2
    for i in range(0, count): #Lucas number algorithm
        three = base + base2
        base = base2
        base2 = three
    return three #Returning value
'''
The fibonacci sequence generator:
ex.: fiSequence(3) = 5 (fourth fibonacci number)
'''
def fiSequence(count):
    # Setting initial values
    base = 0
    base2 = 1
    three = 0
    if count == 0:  #Send 1 if count is zero
        return base2
    for i in range(0, count): #Lucas number algorithm
        three = base + base2
        base = base2
        base2 = three
    return three #Returning value
