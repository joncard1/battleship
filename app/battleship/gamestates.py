import battleship.boardstate as boardstate
import pprint

class GameState(object):
    """
    This is an abstract class that provides an error for each attempted action, which is implemented in sub-classes that support each action.
    """
    
    def place_ship(self, ship_type, base_x, base_y, orientation):
        return 0

    def shoot(self, x, y):
        return 0

class PlaceShip(GameState):
    end = "false"
    success = True
    start = False

    def __init__(self, boardstate, strategy):
        self._boardstate = boardstate
        self._enemy_strategy = strategy

    def place_ship(self, ship_type, base_x, base_y, orientation):
        # if the placement is legal
        #   Get the placement of the enemy ship
        # if the placement is full
        #   Return a new Shoot state
            #return Shoot()
        # else return self
        self._boardstate.place_ship(boardstate.PLAYER_1, ship_type, base_x, base_y, orientation) 
        placement = self._enemy_strategy.get_placement()
        self._boardstate.place_ship(boardstate.PLAYER_2, placement[0], placement[1], placement[2], placement[3])
        if self._boardstate.is_full:
            print "Shooting!"
            new_state = Shoot(self._boardstate, self._enemy_strategy)
        else:
            new_state = self

        new_state.success = True
        return new_state


class Shoot(GameState):
    success = True
    start = True
    end = "false"

    def __init__(self, boardstate, strategy):
        self._boardstate = boardstate
        self._strategy = strategy

    def shoot(self, x, y):
        self.player_hit = self._boardstate.shoot(boardstate.PLAYER_1, x, y)
        # if player 1 didn't win
        if self._boardstate.is_player_dead(boardstate.PLAYER_2):
            return GameWon()
        
        self.server_shot = self._strategy.get_shot()
        self.server_hit = self._boardstate.shoot(boardstate.PLAYER_2, self.server_shot[0], self.server_shot[1])
        if self.server_hit:
            self._strategy.hit()
        else:
            self._strategy.miss()
        if self._boardstate.is_player_dead(boardstate.PLAYER_1):
            return GameLost()

        return self
    

class GameWon(GameState):
    success = True
    player_hit = True
    server_hit = False
    server_shot = "N/A"
    end = "win"

class GameLost(GameState):
    success = True
    player_hit = False
    server_hit = True
    server_shot = "something"
    end = "lost"
