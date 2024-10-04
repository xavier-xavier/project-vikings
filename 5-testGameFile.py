import unittest
from file import Game
from inspect import signature

class TestGame(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.game = Game()
        cls.game.createTeams()

    def testGameCreateTeamsReceiveNoParam(self):
        self.assertEqual(len(signature(self.game.createTeams).parameters), 0)

    def testGameFightReceiveNoParam(self):
        self.assertEqual(len(signature(self.game.fight).parameters), 0)

    def testCreateArmiesWith5Soldiers(self):
        self.assertEqual(len(self.game.war.vikingArmy), 5)
        self.assertEqual(len(self.game.war.saxonArmy), 5)

    def testFightReduceAtLess1Soldier(self):
        self.game.fight()
        initialSoldiers = 5
        self.assertLess(len(self.game.war.vikingArmy), initialSoldiers + 1)
        self.assertLess(len(self.game.war.saxonArmy), initialSoldiers + 1)

    def testFightAtLess1ArmyHasNoSoldiers(self):
        self.game.fight()
        self.assertTrue(len(self.game.war.vikingArmy) == 0 or len(self.game.war.saxonArmy) == 0)


if __name__ == '__main__':
    unittest.main()