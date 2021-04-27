# MILESTONE PROJECT 1: Tic Tac Toe Game

# Build the Visual Representation
# Get the User Input
# Applying the logic for each input
# Update Visual
row1 = []
row2 = []
row3 = []


def play_game():
    game_on = True
    # Welcome to the game message, Enter Player Name, Scores, etc.
    configure_game_options()
    # Initialize a blank board
    create_blank_board()
    # Create a loop with Board Display, Player Prompt
    while game_on:
        display_board()
        prompt_player_input()
        game_on = False
    #


def configure_game_options():
    mode = display_menu()
    if mode == 1:
        # 1 v Computer -- Todo: add ML to play the game (Stretch Goal)
        assign_x_and_o(p1_vs_comp())
    elif mode == 2:
        # Get Player input and assign them to X or O based on
        assign_x_and_o(p1_vs_p2())
    elif mode == 9:
        quit()


def p1_vs_comp():
    p1 = input('Enter Your Name: ')


def p1_vs_p2():
    p1 = input('Enter Player 1 Name: ')
    p2 = input('Enter Player 2 Name: ')
    return {p1: 'X', p2: 'O'}


def assign_x_and_o(players):
    print(players)


def display_board():
    print(row1)
    print(row2)
    print(row3)


def create_blank_board():
    global row1, row2, row3
    row1 = ['1', '2', '3']
    row2 = ['4', '5', '6']
    row3 = ['9', '8', '9']


def prompt_player_input():
    result = int(input('Select your square: '))


def display_menu():
    if row1 == row2 == row3:
        print('|****** Tic-Tac-Toe ******|')
        print('\n')
        print('Please select which mode you would like to participate in.')
        print('1. Self vs Bot (ML in Action)')
        print('2. Player 1 vs Player 2')
    else:
        print('What would you like to do next?')
        print('1. Self vs Bot (ML in Action)')
        print('2. New Player 1 vs Player 2 game')
        print('3. Play Again with no changes')
        print('4. Play Again but switch X and O')
        print('5. Select new symbols for each player')
        print('6. Reset Player Scores to 0')
        print('7. Change Player Names')
        print('8. All configurations at once')
    print('9. Quit Game')
    return int(input('Game Mode: '))


play_game()

