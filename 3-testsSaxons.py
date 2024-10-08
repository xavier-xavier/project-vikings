import unittest
from vikingsClasses import Soldier
from inspect import signature

class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)

    def receiveDamage(self,damage):
        self.health -= damage

        if self.health > 0:
            return f"Un Saxon ha recibido {damage} puntos de daño"
        else:
            return "Un Saxon ha muerto en combate"
class TestSaxon(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.health = 60
        cls.strength = 25
        cls.saxon = Saxon(cls.health, cls.strength)

    def testSaxonShouldReceiveTwoParams(self):
        self.assertEqual(len(signature(Saxon).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.saxon.health, self.health)

    def testStrength(self):
        self.assertEqual(self.saxon.strength, self.strength)

    def testAttack(self):
        self.assertEqual(callable(self.saxon.attack), True)

    def testAttackShouldReceiveNoParams(self):
        self.assertEqual(len(signature(self.saxon.attack).parameters), 0)

    def testAttackREturnStrength(self):
        self.assertEqual(self.saxon.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.saxon.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        self.assertEqual(
            len(signature(self.saxon.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        self.saxon.receiveDamage(1)
        self.assertEqual(self.saxon.health, self.health - 1)

    def testReceiveDamageString45(self):
        self.assertEqual(self.saxon.receiveDamage(
            45), 'Un Saxon ha recibido 45 puntos de daño')

    def testReceiveDamageString10(self):
        self.assertEqual(self.saxon.receiveDamage(
            10), 'Un Saxon ha recibido 10 puntos de daño')

    def testReceiveDamageStringDied(self):
        self.assertEqual(self.saxon.receiveDamage(self.health),
                         'Un Saxon ha muerto en combate')


if __name__ == '__main__':
    unittest.main()
