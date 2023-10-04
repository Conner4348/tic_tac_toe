# ==================================================
# THIS FILE WILL TEST THE FILES ALTOGETHER THUS FAR.
# ==================================================

from check_winner import check_winner_fn as cw
from convert_board import convert_board_fn as convert
from get_input import get_input_fn as get
from get_input import bot_input_fn as bot

game_state = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}

current_round = 0
while current_round < 9:
    get(game_state)
    row = cw(convert(game_state, 0), 'X')
    down = cw(convert(game_state, 1), 'X')
    diag = cw(convert(game_state, 2), 'X')
    if row == True or down == True or diag == True:
        current_round = 9
        break
    current_round += 1
    bot(game_state)
    row = cw(convert(game_state, 0), 'O')
    down = cw(convert(game_state, 1), 'O')
    diag = cw(convert(game_state, 2), 'O')
    if row == True or down == True or diag == True:
        current_round = 9
        break
    current_round += 1