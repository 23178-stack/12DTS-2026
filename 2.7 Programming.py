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
bombs = 5

#Functions
def int_check(min_value,max_value):
    while True:
        try:
            x =int(input("Please enter your choice: "))

            if x < min_value:
                print("\nPlease enter a value in range\n")
                continue

            if x > max_value:
                print("\nPlease enter a value in range\n")
                continue

            return x
        except:
            print("\nPlease enter an integer.")

def instructions():
    print("\nYou have entered the instructions")
    print("""\nWhen selecting targets and other objects, use numerical digits such as 1 to 5

You can quit at any junction by typing "quit" \n""")
    time.sleep(2)
    selection()

def pre_flight():
    global fuel, name, callsign
    print("\n=======Pre Flight Checks=======\n")
    name = input("What is your name brave pilot?: ")
    callsign = input("What is your aircraft's callsign?: ")
    print("\nWelcome aboard", name, "flying", callsign)
    print("""\nDo you wish to carry extra fuel or a repair kit?
[1] Extra Fuel
[2] Repair Kit""")
    choice = int_check(1,2)
    if choice == 1:
        print("\nYou have chosen to carry extra fuel\n")
        fuel = fuel + random.randint(20,50)
        print("You now have", fuel, "litres of fuel")
    elif choice == 2:
        print("\nYou have chosen a repair kit")
        print("You have", fuel, "litres of fuel")
    else:
        print("You have somehow managed to break my code")
    time.sleep(1)
    print("\nTaking off...")
    time.sleep(3)
    print("\nTakeoff successful")
    time.sleep(2)
    bombing_run(grid)

def board_print(board):
    x = 1
    print("\n  1  2  3  4  5")
    for row in board:
        print(x,"  ".join(row))
        x = x+1

def escape():
    print("\nEscape successful")

def bombing_run(board):
    global bombs, damage_taken, fuel, health, target_x, target_y
    print("\n=======BOMBING RUN=======")

    while bombs>0:
        board_print(grid)
        print("\nYou have", bombs, "bombs remaining")
        print("Fuel:", fuel, "L | Damage taken:", damage_taken, "| Health remaining:", health)

        print("\nWhich row would you like to target?")
        row = int_check(1,5)-1
        print("\nWhich column would you like to target?")
        col = int_check(1,5)-1

        if board[row][col] != "-":
            print("\nYou have already targeted this space")
            continue

        elif row == target_x and col == target_y:
            board[row][col] = "X"
            print("\nYou have hit the target location")
            time.sleep(1)
            escape()
            return

        elif row+1 == target_x or row-1 == target_x and col+1 == target_y or col-1 == target_y:
            print("\nNear Miss")
            board[row][col] = "0"
            time.sleep(1)

        else:
            print("\nMiss")
            board[row][col] = "0"
            time.sleep(1)

        if random.randint(1,3)==1:
            print("\nYour bomber has been hit by enemy ground fire!")
            damage_taken = damage_taken + 10
            health = health - 10
            time.sleep(1)

        fuel = fuel - random.randint(10,20)
        bombs = bombs - 1

    print("You lose")

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
        instructions()
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