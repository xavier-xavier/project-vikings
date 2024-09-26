import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health  # la salut del soldat
        self.strength = strength # la força del soldat
    
    def attack(self):
        return self.strength # ens torna la força del soldat

    def receiveDamage(self, damage):
        self.health = self.health - damage # resta el mal que li han fet de la salut


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength) # cridem el constructor de "soldier"
        self.name = name # el nom del viking

    def battleCry(self):
        return "Odin Owns You All!" # crit de guerra del viking

    def receiveDamage(self, damage):
        self.health = self.health - damage # resta el mal rebut de la salut
        if self.health > 0 :
            return f"{self.name} has received {damage} points of damage"
        else :
            return f"{self.name} has died in act of combat"



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength) # cridem el constructor de 'soldier'

    def receiveDamage(self, damage):
        self.health = self.health - damage # restem el mal rebut de la salut del saxó
        if self.health > 0 :
            return f"A Saxon has received {damage} points of damage"
        else :
            return "A Saxon has died in combat"




class War():
    def __init__(self):
        self.vikingArmy = []  # els vikings
        self.saxonArmy = []  # els saxons

    def addViking(self, viking):
        self.vikingArmy.append(viking)  # afegim un viking a l'exèrcit viking
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)  # afegim un saxó a l'exèrcit saxó
    
    def vikingAttack(self):
        if not self.saxonArmy :
            return "No Saxons to attack"

        viking = random.choice(self.vikingArmy)  # triem un viking a l'atzar
        saxon = random.choice(self.saxonArmy)  # triem un saxó a l'atzar
        damage = viking.attack() # obtenim el mal fet al viking
        result = saxon.receiveDamage(damage)  # cridem la funció receiveDamage del saxó amb el paràmetre (damage)

        # ara eliminem els saxons caiguts en batalla
        if saxon.health <= 0 :
            self.saxonArmy.remove(saxon)

        return result


    def saxonAttack(self):
        if not self.vikingArmy :
            return "No vikings"

        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)

        # Eliminem vikings morts
        if viking.health <= 0 :
            self.vikingArmy.remove(viking)

        return result


    def showStatus(self):
        if not self.saxonArmy :
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy :
            return "Saxons have fought for their lives and survive another day..."
        else :
            return "Vikings and Saxons are still in the thick of battle."
    pass


"""
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


"""