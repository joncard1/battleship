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

    def place_ship(self, ship_type, base_x, base_y, orientation):
        # if the placement is legal
        #   Get the placement of the enemy ship
        # if the placement is full
        #   Return a new Shoot state
            #return Shoot()
        # else return self
        if base_y == 1:
            print "moving on?"
            new_state = Shoot()
        else:
            new_state = self
        new_state.success = True
        return new_state

class Shoot(GameState):
    success = True
    start = True

    def shoot(self, x, y):
        return GameLost()

class GameWon(GameState):
    success = True
    end = "win"

class GameLost(GameState):
    success = True
    player_hit = False
    server_hit = True
    server_shot = "something"
    end = "lost"
