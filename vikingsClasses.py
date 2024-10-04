import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        message = ''
        if self.health > 0:
            message = f"{self.name} has received {damage} points of damage"
        else:
            message = f"{self.name} has died in act of combat"
        return message


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            message = f"A Saxon has received {damage} points of damage"
        else:
            message = f"A Saxon has died in combat"
        return message


class War:
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
        result = saxon.receiveDamage(viking.strength)
        for soldier in self.saxonArmy:
            if soldier.health <= 0:
                self.saxonArmy.remove(soldier)

        return result
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = viking.receiveDamage(saxon.strength)
        for soldier in self.vikingArmy:
            if soldier.health <= 0:
                self.vikingArmy.remove(soldier)

        return result

    def showStatus(self):
        if self.vikingArmy and self.saxonArmy:
            return "Vikings and Saxons are still in the thick of battle."
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxonArmy:
            return "Vikings have won the war of the century!"
