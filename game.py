# ==================================================
# THIS FILE WILL TEST THE FILES ALTOGETHER THUS FAR.
# ==================================================

from check_winner import check_winner_fn as cw
from convert_board import convert_board_fn as convert
from get_input import get_input_fn as get
from get_input import bot_input_fn as bot


game_state = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}


print("""

 __      __       .__                                  __                         
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____                 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \                
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )               
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/                
       \/       \/          \/            \/     \/                               
___________.__                   __                            __                 
\__    ___/|__| ____           _/  |______    ____           _/  |_  ____   ____  
  |    |   |  |/ ___\   ______ \   __\__  \ _/ ___\   ______ \   __\/  _ \_/ __ \ 
  |    |   |  \  \___  /_____/  |  |  / __ \\  \___  /_____/  |  | (  <_> )  ___/ 
  |____|   |__|\___  >          |__| (____  /\___  >          |__|  \____/ \___  >
                   \/                     \/     \/                            \/ 

      """)
print('')






current_round = 0
while current_round < 9:
    print('Please select an option from the following choices:')
    print('')
    print_board = convert(game_state, 0)
    for row in print_board:
        print(row)
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

print_board = convert(game_state, 0)
for row in print_board:
    print(row)
print('')
