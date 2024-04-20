import random
from soldier import Soldier

class Viking(Soldier):
    def __init__(self, name, health, strength):
        print('Viking created')

    def battleCry(self):
        print('Odin Owns You All!')

    def receiveDamage(self, damage):
        print('Viking received damage')
