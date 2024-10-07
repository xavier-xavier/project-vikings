import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            #return self.name + ' has received 70 points of damage'
            #return self.name + ' has received 50 points of damage'
            return f'{self.name} has received {damage} points of damage'
        else:
            #return self.name + ' has died in act of combat'
            return f'{self.name} has died in act of combat'
            #self.name + ' has died in act of combat'



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            #return f"Un 'Saxon' ha recibido {damage} puntos de daño."
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'




# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingsArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            
            result = saxon.receiveDamage(viking.attack())

            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)

            return result

    
    def saxonAttack(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)

            result = viking.receiveDamage(saxon.attack())

            if viking.health <= 0:
                self.vikingArmy.remove(viking)

            return result

    def showStatus(self):
        if len(saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        if len(vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'


'''
#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass

'''
