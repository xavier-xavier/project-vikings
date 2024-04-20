import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
    
    def attack(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here

    def battleCry(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        id_viking = random.randrange(len(self.vikingArmy)-1)
        id_saxon = random.randrange(len(self.saxonArmy)-1)

        viking_selected = self.vikingArmy[id_viking]
        saxon_selected = self.saxonArmy[id_saxon]

        result = saxon_selected.receiveDamage(viking_selected.attack())

        if "died in combat" in result:
            self.saxonArmy.pop(id_saxon)
        
        return result

    
    def saxonAttack(self):
        id_viking = random.randrange(len(self.vikingArmy)-1)
        id_saxon = random.randrange(len(self.saxonArmy)-1)

        viking_selected = self.vikingArmy[id_viking]
        saxon_selected = self.saxonArmy[id_saxon]

        result = viking_selected.receiveDamage(saxon_selected.attack())

        if "died in combat" in result:
            self.vikingArmy.pop(id_viking)
        
        return result


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            "Vikings and Saxons are still in the thick of battle."


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


