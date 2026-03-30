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
grid = [
    ["-", "-", "-","-","-"],
    ["-", "-", "-","-","-"],
    ["-", "-", "-","-","-"],
    ["-", "-", "-","-","-"],
    ["-", "-", "-","-","-"]]
target_x = random.randint(0,4)
target_y = random.randint(0,4)

#Functions
def int_check(min_value=None,max_value=None):
    while True:
        try:
            x =int(input("Please enter your choice: "))

            if min_value is not None and x < min_value:
                print("\nPlease enter a value in range\n")
                continue

            if max_value is not None and x > max_value:
                print("\nPlease enter a value in range\n")
                continue

            return x
        except:
            print("\nPlease enter an integer.")

def intructions():
    print("\nYou have entered the instructions")
    print("""\nWhen selecting targets and other objects, use numerical digits such as 1 to 5

You can quit at any junction by typing "quit" \n""")
    time.sleep(2)
    selection()

def takeoff():
    print("\nYou have entered the Takeoff")

def pre_flight():
    global fuel, name, callsign
    print("\n=======Pre Flight Checks=======\n")
    name = input("What is your name brave pilot?: ")
    callsign = input("What is your aircraft's callsign?: ")
    print("Welcome aboard", name, "flying", callsign)
    print("""\nDo you wish to carry extra fuel or a repair kit?
[1] Extra Fuel
[2] Repair Kit""")
    time.sleep(1)
    choice = int_check(1,2)
    if choice == 1:
        print("You have chosen to carry extra fuel")
        fuel = fuel + random.randint(20,40)
        print("You now have", fuel, "litres of fuel")
    elif choice == 2:
        print("You have chosen a repair kit")
    else:
        print("You have somehow managed to break my code")
    time.sleep(1)
    takeoff()

def bombing_run(board):
    for row in board:
        print("  ".join(row))

def selection():
    global welcome_choice
    print("""Make a selection:
[1] : Start a new game
[2] : Instructions
[3] : Quit Game 
""")
    welcome_choice = int_check(1,3)
    if welcome_choice == 1:
        print("\nYou choose to start a new game")
        pre_flight()
    elif welcome_choice == 2:
        print("\nYou have chosen to view the instructions")
        time.sleep(1)
        intructions()
    elif welcome_choice == 3:
        print("\nYou have chosen to quit the game")
        time.sleep(2)
        print("\nGoodbye...\n")
        time.sleep(5)
        welcome()
    else:
        print("This should not display")

def welcome():
    print("""Welcome to the Battle of Britain!

Journey through this game as we learn about some of New Zealand's unsung heros.

There will be a series of puzzles and challenges to complete in order to win.\n""")
    selection()

#Main
welcome()