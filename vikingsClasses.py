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
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return (f"A Saxon has died in combat")
# Davicente

class War():
    def __init__(self):
       self.vikingArmy = []
       self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return saxon.receiveDamage(viking.strength)

    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        return viking.receiveDamage(saxon.strength)


    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        if len(self.vikingArmy) <= 0:
            return "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return "Los Vikingos y los Sajones todavía están en plena batalla."
    pass

thor = Viking("Thor",20,30)
saxon1 = Saxon(30,10)

war = War()

war.addViking(thor)
war.addSaxon(saxon1)
war.showStatus()

war.saxonAttack()
war.showStatus()

war.vikingAttack()
war.showStatus()

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