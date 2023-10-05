# ==================================
# FILE FOR FUNCTION THAT CHECKS
# TO SEE IF THERE IS A WINNER, BASED
# ON THE CURRENT GAME STATE.
# ==================================


def check_winner_fn(game_state, player): # player is the letter that the player is using (X or O)

    for sublist in game_state:
        winner = True # winner holds whether a winner has been found, and is redefined after each iteration.
        for val in sublist: # Loops through each value in a sublist, if a value doesn't equal the player's, then the loop is broken and it moves on to the next sublist.
            if val != player:
                winner = False
                break
        if winner == True: # if the value of winner never changes, then we have found a winner!
            print(f'{player} has won the game!')
            print('')
            return True
    return False