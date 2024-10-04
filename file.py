from vikingsClasses import War, Viking, Saxon

import random

class Game:
    def __init__(self):
        self.war = War()

    """
        Create both armies, vikings and saxons.
    """
    def createTeams(self):
        soldiersName = ['monica', 'noelia', 'alberto', 'gustabo', 'sandra', 'oriol', 'charlie', 'guillermo', 'veronica', 'alba', 'claudia', 'ieva',
                        'Tony', 'jonnathan']

        for i in range(0,5):
            soldierName = random.choice(soldiersName)
            health = 100
            strength = random.randint(20, 100)
            viking = Viking(soldierName, health, strength)
            saxon = Saxon(health, strength)
            self.war.addViking(viking)
            self.war.addSaxon(saxon)

    """
        Fight both armies, vikings and saxons while exist soldiers in both armies.
    """
    def fight(self):
        while self.war.vikingArmy and self.war.saxonArmy:
            if random.choice([True, False]):
                self.war.saxonAttack()
            else:
                self.war.vikingAttack()
            self.war.showStatus()

        self.war.showStatus()


# Launch game
game = Game()
game.createTeams()
game.fight()
