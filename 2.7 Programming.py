#Library
import time
import random

#Constants
MAX_HEALTH = 100
MAX_FUEL = 100

#Variables
health = MAX_HEALTH
fuel = MAX_FUEL
name = ""
callsign = ""
damage_taken = 0
welcome_choice = 0
#Functions
def int_check():
    while True:
        try:
            x =int(input("Please enter your choice: "))
            return x
        except:
            print("Please enter your choice correctly.")





def welcome():
    global welcome_choice
    print("""Welcome to the Battle of Britain!

Journey through this game as we learn about some of New Zealand's unsung heros.

There will be a series of puzzles and challenges to complete in order to win.

Make a selection:
[1] : Start a new game
[2] : Instructions
[3] : Quit Game 
""")
    welcome_choice =int_check()
    if welcome_choice == 1:
        print("You choose to start a new game")
    elif welcome_choice == 2:
        print("You choose to view the instructions")
    else:
        print("You choose to quit the game")
def main():
    welcome()
#Main
main()