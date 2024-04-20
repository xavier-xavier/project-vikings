import random

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if len(self.saxonArmy) == 0:
            print('No saxons alive be attacked')
            return
        if len(self.vikingArmy) == 0:
            print('No viking to attack')
            return

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

    def saxonAttack(self):
        if len(self.vikingArmy) == 0:
            print('No vikings alive be attacked')
            return
        if len(self.saxonArmy) == 0:
            print('No saxon to attack')
            return

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            print("¡Los Vikingos han ganado la guerra del siglo!")
        elif len(self.vikingArmy) == 0:
            print("Los Sajones han luchado por sus vidas y sobreviven otro día...")
        else:
            print("Los Vikingos y los Sajones todavía están en plena batalla.")

    pass
