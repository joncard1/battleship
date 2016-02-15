import random
import battleship.boardstate as boardstate

class EnemyStrategy(object):
    placement_number = 0

    def get_placement(self):
        new_x = random.randint(0, 10)
        new_y = random.randint(0, 10)
        new_orientation = random.choice([boardstate.OR_RIGHT, boardstate.OR_LEFT, boardstate.OR_DOWN, boardstate.OR_UP])
        if self.placement_number == 0:
            new_placement = (
                boardstate.SHIP_BS, 
                new_x,
                new_y,
                new_orientation
            )
        elif self.placement_number <= 2:
            new_placement = (
                boardstate.SHIP_DEST,
                new_x,
                new_y,
                new_orientation
            )
        elif self.placement_number <= 5:
            new_placement = (
                boardstate.SHIP_CR,
                new_x,
                new_y,
                new_orientation
            )
        else:
            new_placement = (
                boardstate.SHIP_FR,
                new_x,
                new_y,
                new_orientation
            )
        self.placement_number += 1
        return new_placement

    def get_shot(self):
        shot_x = random.randint(0, 10)
        shot_y = random.randint(0, 10)
        return (shot_x, shot_y)

    def hit(self):
        pass

    def miss(self):
        pass

class SmarterEnemy(EnemyStrategy):
    ''' This uses the same random placement as the parent strategy, and randomly generates shots, until it has a confirmed hit, then it shoots around that spot'''
    last_hit = None
    next_vector = None

    def get_shot(self):
        if self.last_hit is not None and self.next_vector == 0:
            shot = (self.last_hit[0] + 1, self.last_hit[1])
        elif self.last_hit is not None and self.next_vector == 1:
            shot = (self.last_hit[0], self.last_hit[1] + 1)
        elif self.last_hit is not None and self.next_vector == 2:
            shot = (self.last_hit[0] - 1, self.last_hit[1])
        elif self.last_hit is not None and self.next_vector == 3:
            shot = (self.last_hit[0], self.last_hit[1] - 1)
        else:
            self.last_hit = None
            self.next_vector = None
            shot = super(SmarterEnemy, self).get_shot()

        self.last_shot = shot

        return shot

    def hit(self):
        self.last_hit = self.last_shot
        if self.next_vector is None:
            self.next_vector = 0
            print "Starting surrounding"
        else:
            print "Continuing in this direction"
    
    def miss(self):
        if self.last_hit is not None and self.next_vector < 4:
            print "Trying next direction"
            self.next_vector += 1
        else:
            self.last_hit = None
            self.next_vector = None
