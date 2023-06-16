import random

def rock_paper_scissor():

    chants = ["rock" , "paper" , "scissor"]
    y = [1,2,3]
    choice = random.choice(chants)

    print("rock = 1\npaper = 2\nscissor = 3\nEnter your choice (1/2/3): " , end="")

    try:
        x = int(input(""))        
        while x not in y:
            x = int(input("Please enter a valid input (1/2/3): "))
    except ValueError as error:
        return error

    my_choice = chants[x-1]

    print(f"your_choice : {my_choice}\ncomputer's choice : {choice}")

    if (my_choice == "rock" and choice == "paper") or (my_choice == "paper" and choice == "scissor") or (my_choice == "scissor" and choice == "rock"):
        return "you lost computer won."
    elif my_choice == choice:
        return "no one wins its a tie."
    else:
        return "you won computer lost."
        
a = rock_paper_scissor()
print(a)