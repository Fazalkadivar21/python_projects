import random

def Hangman():
    
    word_list = ["apple" , "money" , "joy" , "love" , "royal" , "colder" , "summer" , "eleveter" , "twelve"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    while tries > 0 :
        display_word = ""

        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"Word : {display_word}")

        if chosen_word == display_word:
            print("Congratulations you have won.")
            break

        guess = input("Guess the letter : ")

        if guess in guessed_letters:
            print("You have already guessed the letter please try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Correct guess")
        else:
            print(f"Wrong guess {tries -1 } tries remaining")
            tries -= 1

    if tries == 0 :
        print(f"You have lost. Zero tries left .The word was {chosen_word}")

Hangman()