#Libraries
import time
import random
import os
#Variables
wild_pokemon = [
    {"Name":"Tepig","Type":"Fire","Level":random.randint(1, 3),"Health":65,"Attack":["Tackle",random.randint(20,40)]},
    {"Name":"Bewear","Type":"Fighting","Level":random.randint(1, 3),"Health":130,"Attack":["Hammer In",random.randint(65,130)]},
    {"Name":"Arceus","Type":"Normal","Level":random.randint(1, 3),"Health":220,"Attack":["Trinity Nova",random.randint(150,200)]},
    {"Name":"Xerneas","Type":"Fairy","Level":random.randint(1, 3),"Health":210,"Attack":["Aurora Beam",random.randint(80,120)]},
    {"Name":"Palafin","Type":"Water","Level":random.randint(1, 3),"Health":340,"Attack":["Giga Impact",random.randint(125,250)]},
    {"Name":"Vivillon","Type":"Bug","Level":random.randint(1, 3),"Health":120,"Attack":["Bug Buzz",random.randint(65,110)]},
    {"Name":"Heliolisk","Type":"Electric","Level":random.randint(1, 3),"Health":120,"Attack":["Powerful Bolt",random.randint(20,70)]}]

own_pokemon = [{"Name":"Skeledirge","Type":"Fire","Level":random.randint(1,3),"Health":340,"Attack":["Vitality Song",random.randint(50,270)]},]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def overworld_timer():
    timer = random.randint(1, 5)
    print(timer)
    time.sleep(timer)
    print("Battle Begins")
    battle()
def battle():
    x=random.randint(0, len(wild_pokemon)-1)
    enemy_pokemon = wild_pokemon[x]
    player_pokemon = own_pokemon[0]
    player_pokemon_hp = player_pokemon["Health"]
    print("Player Pokemon:",player_pokemon["Name"])
    print("Player pokemon HP:",player_pokemon_hp)
    print("A wild",enemy_pokemon["Name"],"appeared")
    print("It's a", enemy_pokemon["Type"], "type pokemon")
    print("It's a Level", enemy_pokemon["Level"], "pokemon")
    print("It has", enemy_pokemon["Health"],"health")

battle()
clear_console()
print("Welcome to Pokemon")