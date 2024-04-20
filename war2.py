import random

class War2():
    def __init__(self, one, two):
        seed = random.randint(0, 1)
        if seed == 0:
            self.vikingCommander = one
            self.saxonCommander = two
        else:
            self.vikingCommander = two
            self.saxonCommander = one

        print('%s lidera los Vikingos' % self.vikingCommander)
        print('%s lidera los Sajones' % self.saxonCommander)

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
            print("¡Los Vikingos liderados por %s han ganado la guerra del siglo!" % self.vikingCommander)
        elif len(self.vikingArmy) == 0:
            print("Los Sajones liderados %s han luchado por sus vidas y sobreviven otro día..." % self.saxonCommander
        else:
            print("Los Vikingos de %s y los Sajones de %s todavía están en plena batalla." % (self.vikingCommander, self.saxonCommander))

    pass

