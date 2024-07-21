import random
from vikingsClasses import Soldier, Viking, Saxon, War

# Function to create teams
def createTeams(war):
    soldier_names = ["Albert", "Andres", "Archie", "Dani", "David", "Gerard", "German", "Graham", "Imanol", "Laura"]
    for i in range(5):
        viking = Viking(random.choice(soldier_names), 100, random.randint(50, 100))
        war.addViking(viking)
    for i in range(5):
        saxon = Saxon(100, random.randint(50, 100))
        war.addSaxon(saxon)

# Function to execute the game
def executeGame():
    war = War()
    createTeams(war)
    round = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"Round {round}")
        print(war.vikingAttack())
        print(war.saxonAttack())
        print(f"Viking army: {len(war.vikingArmy)} warriors, Saxon army: {len(war.saxonArmy)} warriors")
        print(war.showStatus())
        round += 1
    print(war.showStatus())

# Run the game
if __name__ == "__main__":
    executeGame()
