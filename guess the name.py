print("""
   ______                        __  __                                  __             
  / ____/_  _____  __________   / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/    

 """)

from random import randint

Easy_level_turns=10
Hard_level_turns=5

def check_number(guess,number,turns):
    if guess > number:
        print("Too high")
        return turns - 1
    elif guess < number:
        print("Too low")
        return turns - 1
    else:
        print(f"You guessed it right! The number is {number}.")

def set_difficulty():
    level=input('Choose difficulty level:Type "easy" or "hard":')
    if level == "easy":
        return Easy_level_turns
    else:
        return Hard_level_turns

def game():

    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100')

    number=randint(1,100)
    #print(number)

    turns=set_difficulty()
    
    guess=0
    while guess != number:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess=int(input('Make a guess:'))

        turns=check_number(guess,number,turns)
        if turns == 0:
            print("You've run out of guesses,you lose.")
            print(f"The number is {number}.")
            return
        elif guess != number:
            print('Guess again')
game()
