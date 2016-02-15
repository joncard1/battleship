import unittest
import battleship.boardstate as boardstate

class TestBoardState(unittest.TestCase):
    def test_add_ship(self):
        state = boardstate.BoardState()
        state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 1, boardstate.OR_RIGHT)

    def test_shoot_bs_horizontal_hit(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 1, boardstate.OR_RIGHT))
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 1, 1))
    
    def test_shoot_bs_horizontal_hit_2(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 1, boardstate.OR_RIGHT))
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 4, 1))

    def test_shoot_bs_horizontal_miss(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 1, boardstate.OR_RIGHT))
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 5, 1))
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 0, 1))
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 1, 0))

    def test_shoot_bs_vertical_hit(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 1, boardstate.OR_DOWN))
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 1, 2))

    def test_shoot_bs_vertical_rev_hit(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 4, boardstate.OR_UP))
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 1, 3))

    def test_shoot_bs_horizontal_rev_hit(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 4, 1, boardstate.OR_LEFT))
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 3, 1))

    def test_shoot_fr(self):
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_FR, 1, 1, boardstate.OR_RIGHT))
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 0, 1), "Did not miss left")
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 1, 0), "Did not miss high")
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 1, 2), "Did not miss right")
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 2, 1), "Did not miss low")
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 1, 1), "Did not hit")
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 1, 1), "Did not remove ship")

    def test_shoot_twice(self):
        '''
        It should not allow multiple hits to the same spot, but it should not remove the ship until all parts are shot.
        '''
        state = boardstate.BoardState()
        self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 1, 1, boardstate.OR_RIGHT))
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 1, 1), "Did not hit")
        self.assertFalse(state.shoot(boardstate.PLAYER_2, 1, 1), "Should not hit twice")
        self.assertTrue(state.shoot(boardstate.PLAYER_2, 2, 1), "Shold have hit the second time")

    #def test_add_too_many_ships(self):
    #    state = boardstate.BoardState()
    #    self.assertTrue(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 0, 0, boardstate.OR_RIGHT))
    #    self.assertFalse(state.place_ship(boardstate.PLAYER_1, boardstate.SHIP_BS, 0, 2, boardstate.OR_RIGHT))

def suite():
    return unittest.makeSuite(TestBoardState)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
