import random

x = random.randint(1,6)

def dice():
    return x

def high_dice():
    return random.randint(3,6)

def get_6():
    if x == 2 or 3  :
        return x * (6/x)
    
def get_5():
    if x == 1 or 3 :
        return 5
    
def get_4():
    if x == 6 or 2:
        return (x-4)*(x-4)

def get_3():
    if x == 1 or 6:
        if x + 2 > 6:
            return x-2
        else:
            return x+2

def get_2():
    if x == 6 or 4 :
        if (x/2) != 2:
            return x-4
        else:
            return x/2
            
def get_1():
    if x == 3 or 4 or 5:
        return x/x