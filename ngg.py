# import random (this will come in handy)
from random import *

# welcome the user. lol
print ("""
Welcome To My NUMBER GUESSING GAME
**********************************
""")

# use randint to genrate a randome number from 1 to 10
# this will be the computer's guess
comp_guess = randint (1,10)
# print this
print ("I'm thinking of a number between 1 and 10.")

# prompt the user to select a difficulty
difficulty = input ("Choose a difficulty. Type 'easy' or 'hard': ")

# if the difficulty is easy, the user gets 10 guesses
# if the difficulty is hard, the user gets 5 guesses
if difficulty.lower() == 'easy':
    guess = 10
elif difficulty.lower() == 'hard':
    guess = 5

# I'll be using try and except
# incase the user types any other option aside EASY and HARD
try: 
    #create a loop of events that will keep telling the user how many guesses they have
    # as long as the number of guesses is greater than 0
    #the user will also be perpetually prompted to make a guess while (s)he has a guess
    while guess > 0:
        print (f"You have {guess} attempts remaining to guess the answer.")    
        my_guess = int(input ("Make a guess."))  

# if the user's guess is greater than the computer's, it will TOO HIGH
# and the number of guesses reduce by 1 
        if my_guess>comp_guess:
            print ("Too High")
            guess-=1

# if the user's guess is greater than the computer's, it will TOO LOW
# and the number of guesses reduce by 1
        elif my_guess<comp_guess:
            print ("Too Low")
            guess-=1
# if the user guesses correctly, it prints this - and the loop breaks ie. program ends
        else:
            print ("That is freaking correct! You Win.")
            break

# if the difficulty chosen is neither EASY not HARD, it creates a Name Error - which is
# caught and reproduced as THAT'S A WRONG OPTION just before the program ends.
except NameError:
    print ("That's a wrong option.")
