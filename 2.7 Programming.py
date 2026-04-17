#==========Library==========

import time
import random

#==========Constants==========

MAX_HEALTH = 100
STARTING_FUEL = 100

#==========Variables==========

health = MAX_HEALTH
fuel = STARTING_FUEL
name = ""
callsign = ""
damage_taken = 0
welcome_choice = 0
grid = [
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"],
    ["-", "-", "-","-","-", "-", "-","-","-"]]

target_x = random.randint(0,4)
target_y = random.randint(0,4)
bombs = 10

#==========Functions==========
def int_check(min_value,max_value): #this code is used for taking user inputs and checking if they are integers as well as if they are in range
    while True:
        try:
            x =int(input("Please enter your choice: ")) #this takes the input and checks if integer

            if x < min_value: #this checks of it is smaller than the min input normally 1
                print("\nPlease enter a value in range\n")
                continue

            if x > max_value: #this checks if larger than max input
                print("\nPlease enter a value in range\n")
                continue

            return x
        except: #this rejects the input if it doesnt meet the criteria and starts from the top
            print("\nPlease enter an integer.")

def instructions(): #This function shows the user the instructions and feeds them back to the selection page once done
    print("\nYou have entered the instructions")
    print("""\nWhen selecting targets and other objects, use numerical digits such as 1 to 5

You can quit at any junction by typing "quit" \n""")
    time.sleep(2)
    selection()

def pre_flight(): #this function sets up the player, they choose their name and callsign as well as items
    global fuel, name, callsign
    print("\n=======Pre Flight Checks=======\n")
    name = input("What is your name brave pilot?: ")    #this lets them choose their name
    callsign = input("What is your aircraft's callsign?: ") #this lets them choose their callsign
    print("\nWelcome aboard", name, "flying", callsign)
    print("""\nDo you wish to carry extra fuel or a repair kit? 
[1] Extra Fuel
[2] Repair Kit""") #this lets them choose either extra fuel or a repair kit
    choice = int_check(1,2)
    if choice == 1: #this randomly adds between 20 and 50 litres of fuel if they choose this
        print("\nYou have chosen to carry extra fuel\n")
        fuel = fuel + random.randint(20,50)
        print("You now have", fuel, "litres of fuel")
    elif choice == 2: # this adds a repair kit if they choose it
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

def board_print(board): # this prints the board along with numbers to make it easy to pick your target
    x = 1
    print("\n  1  2  3  4  5  6  7  8  9")
    for row in board:
        print(x,"  ".join(row))
        x = x+1

def escape(): #this is a small cut scene
    print("\nEscape successful")
    print("\nYou have completed the game")
    print("\nCongratulations")
    time.sleep(2)
    welcome()

def bombing_run(board): #this is the bombing run code
    global bombs, damage_taken, fuel, health, target_x, target_y
    print("\n=======BOMBING RUN=======")

    while bombs>0: #this runs while you have more than 0 bombs
        board_print(grid)
        print("\nYou have", bombs, "bombs remaining") #this is a read out of your current stats that you get at the start of  each bomb drop
        print("Fuel:", fuel, "L | Damage taken:", damage_taken, "| Health remaining:", health)
#this is where you choose what row and coloum to target
        print("\nWhich row would you like to target?")
        row = int_check(1,9)-1
        print("\nWhich column would you like to target?")
        col = int_check(1,9)-1

        if board[row][col] != "-": #this checks if you have already targeted the location
            print("\nYou have already targeted this space")
            continue

        elif row == target_x and col == target_y: #this checks if you hit the location
            board[row][col] = "X"
            print("\nYou have hit the target location")
            board_print(grid)
            time.sleep(1)
            escape()
            return

        elif row+1 == target_x or row-1 == target_x and col+1 == target_y or col-1 == target_y: #this checks if you were close to the target and lets you know
            print("\nNear Miss")
            board[row][col] = "0"
            time.sleep(1)

        else:
            print("\nMiss") #this just tells you that you missed
            board[row][col] = "0"
            time.sleep(1)

        if random.randint(1,3)==1: # this will randomly damage your bomber on each bomb drop
            print("\nYour bomber has been hit by enemy ground fire!")
            damage_taken = damage_taken + 10
            health = health - 10
            time.sleep(1)

        fuel = fuel - random.randint(10,20)
        bombs = bombs - 1

        if fuel < 0:
            print("\nGame over, you are out of fuel")
            welcome()

    print("\nOut of bombs")
    time.sleep(0.5)
    print("\nYou lose")
    time.sleep(0.5)
    print("\nThe target was at", target_x, target_y)
    board[target_x][target_y] = "X"
    board_print(grid)
    time.sleep(1)
    welcome()

def selection(): # this lets the player select what part of the game they want
    global welcome_choice
    print("""Make a selection:
[1] : Start a new game
[2] : Instructions
[3] : Quit Game 
""")
    welcome_choice = int_check(1,3)
    if welcome_choice == 1: # This lets them start a new game
        print("\nYou choose to start a new game")
        pre_flight()
    elif welcome_choice == 2: #this lets them view the instructions
        print("\nYou have chosen to view the instructions")
        time.sleep(1)
        instructions()
    elif welcome_choice == 3: #this lets them restart the game
        print("\nYou have chosen to quit the game")
        time.sleep(2)
        print("\nGoodbye...\n")
        time.sleep(5)
        welcome()
    else:
        print("This should not display")

def welcome(): # this welcomes the player to the game and informs them about what will happen
    print("""Welcome to the Battle of Britain!

Journey through this game as we learn about some of New Zealand's unsung heros.

There will be a series of puzzles and challenges to complete in order to win.\n""")
    selection()

#==========Main==========
welcome()