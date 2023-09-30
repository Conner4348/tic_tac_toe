# ===================================================
# THIS FILE WILL HOLD A FUNCTION THAT
# TAKES A DICTIONARY SHOWING THE CURRENT GAME STATE
# AND WILL CONVERT IT INTO A LIST CONTAINING SUBLISTS
# FOR EITHER EACH ROW, COLUMN OR DIAGONAL.
# ===================================================

# Create a function that takes the game state and
# how you want the board to be configured (0=across, 1=vertical, 2=diagonal).

def convert_board(game_state, config):

  board_config = []

  if config == 0:
    current_sub = []
    for val in game_state.values():
      current_sub.append(val)
      if len(current_sub) == 3:
        board_config.append(current_sub)
        current_sub = []
    print(board_config)
    return board_config

  if config == 1:
    current_sub = []
    current_index = 0
    for key, val in game_state.items():
      pass
      # WRITE PSEUDOCODE FOR THIS PART
      # BEFORE TRYING TO TACKLE REST.

  if config == 2:
    pass



# =======
# TESTING
# =======

test_one = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

fn_test_one = convert_board(test_one, 0)