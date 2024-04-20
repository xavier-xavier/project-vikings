import random
from soldier import Soldier

class Saxon(Soldier):
    def __init__(self, health, strength):
        print('Saxon created')

    def receiveDamage(self, damage):
        print('Saxon received damage')

