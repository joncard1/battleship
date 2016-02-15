import unittest
import battleship.strategies as strategies
import battleship.boardstate as boardstate

class TestStrategies(unittest.TestCase):
    def test_get_placement(self):
        strategy = strategies.EnemyStrategy()
        placement = strategy.get_placement()
        self.assertEqual(placement[0], boardstate.SHIP_BS, "Did not get battleship first")
        self.assertIn(placement[3], [boardstate.OR_LEFT, boardstate.OR_DOWN, boardstate.OR_RIGHT, boardstate.OR_UP])
        for i in range(0, 2):
            placement = strategy.get_placement()
            self.assertEqual(placement[0], boardstate.SHIP_DEST, "Did not get a destroyer second")
        for i in range(0, 3):
            placement = strategy.get_placement()
            self.assertEqual(placement[0], boardstate.SHIP_CR, "Did not get a cruiser third")
        for i in range(0, 4):
            placement = strategy.get_placement()
            self.assertEqual(placement[0], boardstate.SHIP_FR, "Did not get a frigate fourth")

    def test_get_shot(self):
        strategy = strategies.EnemyStrategy()
        shot = strategy.get_shot()
        self.assertIsNotNone(shot)
        
def suite():
    return unittest.makeSuite(TestStrategies)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
