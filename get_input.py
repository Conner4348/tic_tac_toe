# ====================================================
# FUNCTION FOR COLLECTING PLAYER INPUT FOR TIC-TAC-TOE
# ====================================================

# Should take user input from a range of 0-8 and convert that input
# into two different indices: # sublist (0-2 or 0-1) and # within sublist (0-2).
# example: [[0, 1, 2], [3, 4, 5], [6, 7, 8]], the input of 6 should be converted to values: 2 (sublist index), 0 (value index).
# Function should also recursively call itself if the value is not found in list.

# I am going to have the backend board be a dictionary instead for easier retrieval.

from random import choice
from convert_board import convert_board_fn as convert

def get_input_fn(game_state):
    
    choice = int(input())
    if choice not in list(game_state.keys()):
        print(f'Sorry, {choice} is not an option, please enter a valid choice.')
        get_input_fn(game_state)
    if game_state[choice] == None:
        game_state[choice] = 'X'
        #print(game_state)
    else:
        print(f'Sorry {choice} is already taken.')
        get_input_fn(game_state)
    print('')
    print('Current state of board:')
    print('')
    display = convert(game_state, 0)
    for row in display:
        print(row)
    print('')

    #for sublist_index in reversed(range(len(game_state))):
    #    for value in game_state[sublist_index]:
    #        if value >= choice:
    #            pass

def bot_input_fn(game_state):

    available = []
    for key, val in game_state.items():
        if val == None:
            available.append(key)
    if len(available) == 0:
        return
    bot_choice = choice(available)
    game_state[bot_choice] = 'O'
    print(f'The bot has chosen {bot_choice}')
    #print(game_state)
    print('')
    print('Current state of board:')
    print('')
    display = convert(game_state, 0)
    for row in display:
        print(row)
    print('')



# =======
# TESTING
# =======

test_one = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}

#fn_test_one = get_input(test_one)
#fn_test_two = bot_input(test_one)