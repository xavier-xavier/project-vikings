import random
from astropy.io.fits import append

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
        super().__init__(health,strength)
        self.name = name

    def attack(self):
        return self.strength

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
        super().__init__(health,strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


'''
v1 = Viking ("Pepe el terrible", 100, 100)
print(v1.battleCry())
print (v1.attack())
print(v1.receiveDamage(50))
print(v1.health)
print(v1.strength)
print(v1.receiveDamage(50))
print(v1.health)
print(v1.strength)

s1 = Saxon (100, 100)
print (s1.attack())
print(s1.receiveDamage(50))
print(s1.health)
print(s1.strength)
print(s1.receiveDamage(50))
print(s1.health)
print(s1.strength)
'''


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
        #Soldados aleatorios
        VkIndex=random.randrange(0, len(self.vikingArmy))
        Vikingo = self.vikingArmy[VkIndex]
        SjIndex=random.randrange(0,len(self.saxonArmy))
        Sajon=self.saxonArmy[SjIndex]
        #Daño
        Dano=Sajon.receiveDamage(Vikingo.strength)
        #Muerte
        if Sajon.health <= 0:
            del self.saxonArmy[SjIndex]
        #Status
        print(VkIndex, Vikingo.name, SjIndex, Sajon.health)
        return Dano
    
    def saxonAttack(self):
        #Soldados aleatorios
        VkIndex=random.randrange(0, len(self.vikingArmy))
        Vikingo = self.vikingArmy[VkIndex]
        SjIndex=random.randrange(0,len(self.saxonArmy))
        Sajon=self.saxonArmy[SjIndex]
        #Daño
        Dano=Vikingo.receiveDamage(Sajon.strength)
        #Muerte
        if Vikingo.health <= 0:
            del self.vikingArmy[VkIndex]
        #Status
        print(f"S{SjIndex}", Sajon.strength, VkIndex, Vikingo.name, Vikingo.health )
        return Dano

    def showStatus(self):
        VkSt=len(self.vikingArmy)
        SxSt=len(self.saxonArmy)
        print(f"Hay {VkSt} vikingos y {SxSt} sajones en guerra")
        if VkSt >0 and SxSt == 0:
            return "Vikings have won the war of the century!"
        if SxSt >0 and VkSt == 0:
            return "Saxons have fought for their lives and survive another day..."
        if VkSt >0 and SxSt > 0:
            return "Vikings and Saxons are still in the thick of battle."
    pass


v1 = Viking ("Pepe el terrible", 500, 150)
v2 = Viking ("Churro el sanguinario", 500, 200)
v3 = Viking ("Cuernecitos", 500, 50)
s1 = Saxon (500, 100)
s2 = Saxon (500, 120)
s3 = Saxon (500, 70)

Guerra = War()
War.addViking(Guerra,v1)
War.addViking(Guerra,v2)
War.addViking(Guerra,v3)
War.addSaxon(Guerra,s1)
War.addSaxon(Guerra,s2)
War.addSaxon(Guerra,s3)

for i in range (1,50):
    if random.randrange(0, 2)==0:
        print("Atacan Vikingos")
        print(Guerra.vikingAttack())
    else:
        print("Atacan Sajones")
        print(Guerra.saxonAttack())
    print(Guerra.showStatus())
    #Termina Guerra
    if len(Guerra.vikingArmy)==0 or len(Guerra.saxonArmy)==0 :
        break

