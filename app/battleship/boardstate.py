# TODO: Some constants here to provide the vocabulary of ships?

class BoardState(object):
    player1_board = {}
    player2_board = {}

    def place_ship(self, player, base_x, base_y, orientation):
        # TODO: Validate that the ship placement is legal
            # Does not go off the board
            # Does not touch another ship
            # Does not cross another ship
        # TODO: Store the location
        pass

    def shoot(self, player, shot_x, shot_y):
        # TODO: Validate collision
        #   Remember to use other board!
        # return true or false depending on hit
        pass
