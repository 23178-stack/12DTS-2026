# Variables
user_turn = 'O'
position = 0
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]]


# Functions
def print_board(board):  # board printing function
    for row in board:
        print(" | ".join(row))

def position_setter(x):
    vbnm

def user_input():
    global user_turn
    global position
    global board

    while True:
        try:
            position = int(input(f"Player {user_turn} enter position (1-9): "))
            break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# ============MAIN=========================
print("""Welcome to Tic Tac Toe!
When deciding where to place your X or O please reference the below grid
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

""")
print_board(board)
user_input()
