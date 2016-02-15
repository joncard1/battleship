# TODO: Some constants here to provide the vocabulary of ships?
import pprint

OR_RIGHT = 0
OR_LEFT = 1
OR_DOWN = 2
OR_UP = 3

PLAYER_1 = 0
PLAYER_2 = 1

SHIP_BS = 0
SHIP_DEST = 1
SHIP_CR = 2
SHIP_FR = 3

LENGTHS = [4, 3, 2, 1]

class BoardState(object):
    players = [] 
    is_full = False

    def __init__(self):
        self.players = [{"ships": [], "parts": {} }, {"ships": [], "parts":{} }]

    def place_ship(self, player, ship_type, base_x, base_y, orientation):
        # TODO: Validate that the ship placement is legal
            # Does not go off the board
            # Does not touch another ship
            # Does not cross another ship
            # Does not have too many of the same ship
                # Iterate over the ships collection
        # Store the location
        new_ship = Ship(ship_type)
        self.players[player]['ships'].append(new_ship)
        step_x = (-2) * (1 & orientation) * ((orientation ^ 2) >> 1) + ((orientation ^ 2) >> 1)
        step_y = (-2) * (1 & orientation) * (orientation >> 1) + (orientation >> 1)
        part_index = 0
        if step_x != 0:
            x_range = range(base_x, base_x + LENGTHS[ship_type] * step_x, step_x)
        else:
            x_range = [base_x]
    
        if step_y != 0:
           y_range = range(base_y, base_y + LENGTHS[ship_type] * step_y, step_y)
        else:
            y_range = [base_y]

        for new_x in x_range:
            for new_y in y_range:
                if new_x not in self.players[player]['parts']:
                    self.players[player]['parts'][new_x] = {}
                if new_y not in self.players[player]['parts'][new_x]:
                    self.players[player]['parts'][new_x][new_y] = new_ship.parts[part_index]
                    part_index += 1
                else:
                    # Ship was placed twice. BAD
                    pass

        #if ship_type in self.players[player]:
        #   self.players[player][ship_type].append((base_x, base_y, orientation))
        #else:
        #self.players[player][ship_type] = [(base_x, base_y, orientation)]
        self.is_full = True
        for player in self.players:
            if len(player['ships']) != 10:
                self.is_full = False
                break
            
        return True

    def shoot(self, player, shot_x, shot_y):
        ''' Returns True or False to indicate a hit '''
        print "Player %s not player %s" % (int(not player), player)
        target_player = self.players[int(not player)]
        pprint.pprint(target_player['parts'])
        if shot_x in target_player['parts']:
            if shot_y in target_player['parts'][shot_x]:
                if target_player['parts'][shot_x][shot_y].hit:
                    print "Already hit here"
                    pass # Hit twice
                else:
                    print "Hit!"
                    target_player['parts'][shot_x][shot_y].hit = True
                    return True
            else:
                print "No parts at %s" % shot_y
        else:
            print "No parts at %s" % shot_x

        return False

class Ship(object):
    parts = []

    def __init__(self, ship_type):
        self.parts = []
        for i in range(0, LENGTHS[ship_type]):
            self.parts.append(ShipPart())

class ShipPart(object):
    hit = False
