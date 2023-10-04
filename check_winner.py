# ==================================
# FILE FOR FUNCTION THAT CHECKS
# TO SEE IF THERE IS A WINNER, BASED
# ON THE CURRENT GAME STATE.
# ==================================

# Create a function that will check if there is a winner based
# on some test inputs.
# Example:
# input: [[X, X, X], [3, O, O], [6, X, O]]
# The function should look at this input and return if one of the sublists
# has all of the same value.
# Should return True, because the first sublist's values are all equal.

# Maybe try dictionary to store game state.
# {True: [X, X, X], False: [3, O, O], False: [6, X, O]}
# A key of True means that all spots have been taken in the sublist.
# A key of Flase means not all spots have been taken in the sublist.

# PSEUDOCODE
# One loop cycles through each sublist, while a nested loop cycles through each value in each index.
# The nested loop should terminate if a value is found that does not match the player value.
# If the nested loop is not terminated, then all loops should be broken and the function
# will return True.
# If the nested loops are all terminated, then the function should return False.

def check_winner_fn(game_state, player): # player is the letter that the player is using (X or O)

    winner = None
    for sublist in game_state:
        if winner == True:
            print(f'{player} has won the game!')
            return True
        winner = True
        for val in sublist:
            if val != player:
                #print(f'{val} does not match {player}.')
                winner = False
                continue
        
    #print(f'{player} has not won the game...')
    return False

# =======
# TESTING
# =======

test_one = [['X', 'X', 'X'], [3, 'O', 'O'], [6, 'X', 'O']]
test_two = [['X', 'X', 2], ['X', 'O', 'O'], [6, 'X', 'O']]
test_three = [['O', 'O', 2], ['X', 'X', 'X'], [6, 'X', 'O']]

#print('The following two tests should return True, False, True:')
#fn_one = check_winner(test_one, 'X')
#fn_two = check_winner(test_two, 'X')
#fn_three = check_winner(test_three, 'X')