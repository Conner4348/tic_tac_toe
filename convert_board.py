# ===================================================
# THIS FILE WILL HOLD A FUNCTION THAT
# TAKES A DICTIONARY SHOWING THE CURRENT GAME STATE
# AND WILL CONVERT IT INTO A LIST CONTAINING SUBLISTS
# FOR EITHER EACH ROW, COLUMN OR DIAGONAL.
# ===================================================


def convert_board_fn(game_state, config): # Function takes the current game_state (dictionary) and config for how you want to arrange the board (0=rows, 1=columns, 2=diagonals)

  board_config = [] # board_config will hold the arrangement of the board.

  if config == 0:
    current_sub = [] # current_sub will hold each sublist of either a row, column or diagonal.
    for val in game_state.values():
      current_sub.append(val) # each value of the board gets appended, until current_sub has 3 values.
      if len(current_sub) == 3:
        board_config.append(current_sub) # current_sub is then appended to the board_config and current_sub is redefined as empty for the next values.
        current_sub = []
    return board_config

  if config == 1:
    current_sub = []
    current_index = 0
    current_loop = 1
    while current_loop <= 3:
      current_sub.append(game_state[current_index])
      current_index += 3
      if current_index >= len(game_state.keys()):
        board_config.append(current_sub)
        current_sub = []
        current_index -= 8
        current_loop += 1
    return board_config



  if config == 2:
    
    current_sub = []
    current_index = 0
    current_dif = 4
    while len(board_config) < 2:
      current_sub.append(game_state[current_index])
      if len(current_sub) == 3:
        board_config.append(current_sub)
        current_sub = []
        current_dif = -2
      current_index = current_index + current_dif
    return board_config
  





# =======
# TESTING
# =======

#test_one = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

#fn_test_one = convert_board_fn(test_one, 0)
#fn_test_two = convert_board_fn(test_one, 1)
#fn_test_three = convert_board_fn(test_one, 2)