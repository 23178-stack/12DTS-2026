#Libraries
import time
import random
#Variables
wild_pokemon = [
    {"Name":"Tepig","Type":"Fire","Level":random.randint(1, 3),"Health":65,"Attack":["Tackle",random.randint(20,40)]},
    {"Name":"Bewear","Type":"Fighting type","Level":random.randint(1, 3),"Health":65,"Attack":["Tackle",random.randint(20,40)]},
    {"Name":"Tepig","Type":"Fire","Level":random.randint(1, 3),"Health":65,"Attack":["Tackle",random.randint(20,40)]}
]




own_pokemon =

def overworld_timer():
    timer = random.randint(1, 5)
    print(timer)
    time.sleep(timer)
    print("Battle Begins")
    battle()
def battle():
    x=random.randint(0, len(wild_pokemon)-1)
    enemy_pokemon = wild_pokemon[x]
    player_pokemom = own_pokemon
    player_pokemom_hp = player_pokemom["Health"]
    print("Player Pokemon:",player_pokemom["Name"])
    print("Player pokemon HP:",player_pokemom_hp)
    print("A wild",enemy_pokemon["Name"],"appeared")
    print("It's a", enemy_pokemon["Type"], "type pokemon")
    print("It's a level", enemy_pokemon["Level"])
    print("It has", enemy_pokemon["Health"])

