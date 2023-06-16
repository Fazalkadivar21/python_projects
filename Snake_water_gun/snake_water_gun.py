import random

def snake_water_gun():

    chants = ["snake" , "water" , "gun"]
    y = [1,2,3]
    choice = random.choice(chants)

    print("Snake = 1\nWater = 2\nGun = 3\nEnter your choice (1/2/3): " , end="")

    try:
        x = int(input(""))        
        while x not in y:
            x = int(input("Please enter a valid input (1/2/3): "))
    except ValueError as error:
        return error

    my_choice = chants[x-1]

    print(f"your choice : {my_choice}\ncomputer's choice : {choice}")

    if (my_choice == "snake" and choice == "water") or (my_choice == "water" and choice == "gun") or (my_choice == "gun" and choice == "snake"):
        return "you lost computer won."
    elif my_choice == choice:
        return "no one wins its a tie."
    else:
        return "you won computer lost."
        
a = snake_water_gun()
print(a)
