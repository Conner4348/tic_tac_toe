# ==================================================
# THIS FILE WILL TEST THE FILES ALTOGETHER THUS FAR.
# ==================================================

from check_winner import check_winner as cw
from convert_board import convert_board as convert
from get_input import get_input as get
from get_input import bot_input as bot

game_state = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}

get(game_state)
cw(convert(game_state, 0), 'X')
cw(convert(game_state, 1), 'X')
cw(convert(game_state, 2), 'X')
bot(game_state)
cw(convert(game_state, 0), 'O')
cw(convert(game_state, 1), 'O')
cw(convert(game_state, 2), 'O')