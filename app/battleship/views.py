from pyramid.view import view_config
import json
from battleship.gamestates import PlaceShip
from battleship.boardstate import BoardState
from battleship.strategies import EnemyStrategy, SmarterEnemy

ERROR_STATE = 0
WIN_STATE = 1
LOSE_STATE = 2

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'battleship'}

@view_config(route_name='start', renderer='templates/start.pt')
def start(request):
    session = request.session
    boardstate = BoardState()
    strategy = SmarterEnemy()
    session['state'] = PlaceShip(boardstate, strategy)
    # TODO: Instantiate opposing strategy
    return {'success': json.dumps(True)}

@view_config(route_name='place_ship', renderer='templates/place_ship.pt')
def place_ship(request):
    ship_type = int(request.params['type'])
    base_x = int(request.params['base_x'])
    base_y = int(request.params['base_y'])
    orientation = int(request.params['orientation'])
    session = request.session
    state = session['state']
    new_state = state.place_ship(ship_type, base_x, base_y, orientation)
    if new_state == ERROR_STATE:
        return {
            'success': json.dumps(False),
            'start': json.dumps(False)
        }
    else:
        session['state'] = new_state
        return {
            'success': json.dumps(new_state.success),
            'start': json.dumps(new_state.start)
        }

@view_config(route_name='shoot', renderer='templates/shoot.pt')
def shoot(request):
    # Get the coordinates
    x = int(request.params['x'])
    y = int(request.params['y'])

    # TODO: Evaluate if hit
    session = request.session
    state = session['state']
    new_state = state.shoot(x, y)
    if new_state == ERROR_STATE:
        return {
            'success': json.dumps(False)
        }
    else:
        return {
            'success': json.dumps(new_state.success),
            'player_hit': json.dumps(new_state.player_hit),
            'server_shot': json.dumps(new_state.server_shot),
            'server_hit': json.dumps(new_state.server_hit),
            'end': json.dumps(new_state.end)
        }
