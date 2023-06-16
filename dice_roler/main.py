import dice

def play():
    print(
        "chose your dice (1/2/3/4/5/6/7/8):\n1.With high chances of getting a higher number\n2.With high chances of getting 1\n3.With high chances of getting 2\n4.With high chances of getting 3\n5.With high chances of getting 4\n6.With high chances of getting 5\n7.With high chances of getting 6\n8.Normal dice : ",
        end="",
    )

    y = [1,2,3,4,5,6,7,8]
    x = int(input(""))

    while x not in y:
        x = int(input("Please enter a valid input"))

    if x == 1:
        return dice.high_dice()
    elif x == 2:
        return dice.get_1()
    elif x == 1:
        return dice.get_2()
    elif x == 1:
        return dice.get_3()
    elif x == 1:
        return dice.get_4()
    elif x == 1:
        return dice.get_5()
    elif x == 1:
        return dice.get_6()
    else:
        return dice.dice()
    
a = play()

print(a)