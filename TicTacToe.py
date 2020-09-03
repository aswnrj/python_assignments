from IPython.display import clear_output


# THIS FUNCTION RUNS AFTER EACH INPUT FROM PLAYERS AND UPDATES THE BOARD
def display_board(board):
    clear_output()
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("   |   |   ")
    print("--- --- ---")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("   |   |   ")
    print("--- --- ---")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))
    print("   |   |   ")


# THIS FUNCTION HELPS THE PLAYERS TO CHOSE THEIR PREFERRED MARKER (X or O)
def player_input():
    userInput = input("Choose X or O: ")
    while userInput not in ['X', 'O']:
        userInput = input("Enter a valid input: ")
    if userInput == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# THIS FUNCTION PLACES THE MARKER IN THE BOARD GIVEN THE BOARD, THE MARKER AND THE INDEX
def place_marker(board, marker, position):
    board[position] = marker


# THIS FUNCTIONS RUNS AFTER EACH INPUT TO CHECK WHETHER ANY OF THE PLAYERS HAVE WON
def win_check(b, m):
    if [m, m, m] in [b[1:4], b[4:7], b[7:10], [b[1], b[4], b[7]], [b[2], b[5], b[8]], [b[3], b[6], b[9]], [b[1], b[5], b[9]], [b[3], b[5], b[7]]]:
        return True
    else:
        return False


# AFTER GETTING A POSITION INPUT FROM THE PLAYER, THIS FUNCTION CHECKS WHETHER THE GIVEN POSITION IS FREE OR NOT
def space_check(board, position):
    return board[position] == " "


# THIS CHECKS WHETHER ALL THE INDEXES OF THE BOARD HAVE BEEN FILLED
def full_board_check(board):
    for space in board:
        if space == " ":
            return False
    return True


# ASKS THE USER TO ENTER AN INPUT UNTIL THE USER ENTERS AN UNFILLED POSITION WHERE THEY WANT TO PLACE THEIR MARKER
def player_choice(board):
    pos = int(input("Choose a position from 1-9 (1 signifies top left box): "))
    if space_check(board, pos):
        return pos
    else:
        print("That square is occupied")
    return player_choice(board)


# ASKS THE USER WHETHER THEY WANT TO PLAY ANOTHER GAME
def replay():
    var = input("Do you want to play again? Enter Y or N: ")
    if var == 'Y':
        return True
    elif var == 'N':
        return False
    else:
        print("Enter a valid input")
        replay()


# THE MAIN FUNCTION USED TO RUN TIC-TAC-TOE GAME
def tic_tac_toe():
    test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    gameOn = True
    print("Player1's choice :")
    choiceList = player_input()
    print(f"So Player1 has chosen {choiceList[0]}")

    # THIS LOOP CONTINUES UNTIL EITHER OF THE PLAYERS WIN OR THE BOARD GETS COMPLETELY FILLED
    while gameOn and not (full_board_check(test_board) or win_check(test_board, 'X') or win_check(test_board, 'O')):

        # INPUTTING, STORING AND DISPLAYING PLAYER 1'S CHOICE
        print("Player1's turn: ")
        pos1 = player_choice(test_board)
        place_marker(test_board, choiceList[0], pos1)
        display_board(test_board)
        if win_check(test_board, choiceList[0]):
            print("Player1 wins")
        elif full_board_check(test_board):
            print('The Game is a draw')
        else:

            # INPUTTING, STORING AND DISPLAYING PLAYER 2'S CHOICE AS LONG AS PLAYER 1 HASN'T WON YET
            print("Player2's turn:")
            pos2 = player_choice(test_board)
            place_marker(test_board, choiceList[1], pos2)
            display_board(test_board)
            if win_check(test_board, choiceList[1]):
                print("Player2 wins")
            elif full_board_check(test_board):
                print('The Game is a draw')

    # ASKING THE USER WHETHER THEY WOULD LIKE ANOTHER GAME
    gameOn = replay()
    if gameOn:
        tic_tac_toe()


tic_tac_toe()
