import time
import random

#Constants
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
SUITS = ["Hearts", "Clubs", "Spades", "Diamonds"]

#Variables
deck = [[], []]
hand = [[], []]
hand_size = 0

#Functions
def deck_printer():
    for i in range(0, len(deck[0])):
        print("Card", i, "is the", deck[1][i], "of", deck[0][i])
        time.sleep(0.3)

def hand_builder(x):
    print("Drawing cards:")
    for i in range(0, x):
        y = random.randint(0,len(deck[0]))
        hand[0].append(deck[0][x])
        deck[0].pop(x)
        hand[1].append(deck[1][x])
        deck[1].pop(x)

def hand_printer():
    dcfg

#----------START--------------
#Deck Builder
print("Building Deck...")
for x in SUITS:
    print("---Adding:", x, "suit.")
    for y in VALUES:
        deck[0].append(x)
        deck[1].append(y)
        print("Card:", y, "of", x, "added")
        time.sleep(0.3)
    print("---Done!")
deck_printer()
hand_size = int(input("How many cards do you want in your deck?: "))
hand_builder(hand_size)