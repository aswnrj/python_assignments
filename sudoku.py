# THIS 9*9 ARRAY OF ZEROS REPRESENTS THE SUDOKU BOARD. EDIT THIS WITH THE BOARD YOU WANT TO SOLVE
# ADD THE NUMBERS IN THEIR RESPECTIVE POSITIONS(LEAVE THE ZEROS AS IT IS INSTEAD OF BLANK SPACES)

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# THIS REPRESENTS THE NUMBER OF NON ZERO NUMBERS YOU HAVE ADDED
n_numbers = 0

num_zeros = 81 - n_numbers


# CREATES AN ARRAY REPRESENTING EACH 3*3 BOX GIVEN TOP LEFT INDEX
def box(board, i, j):
    ans = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
    return ans


# PRINTS THE BOARD AFTER SOLVING
def print_board(board):
    for i in range(9):
        print(*board[i][:3], " | ", *board[i][3:6], " | ", *board[i][6:])
        if i % 3 + 1 == 3 and i != 8:
            print("- - - - - - - - - - - - -")


# CHECK WHETHER THE NUMBER CAN BE PLACED IN THE GIVEN POSITION
def iscorrect(board, i, j, num):
    if num in board[i]:
        return False
    for t in range(9):
        if board[t][j] == num:
            return False
    boxi = (i // 3) * 3
    boxj = (j // 3) * 3
    if num in box(board, boxi, boxj):
        return False

    return True


# THE MAIN FUNCTION WHICH RUNS UNTIL ALL BOXES ARE FILLED
def sudoku(board, nzeros, row, col):
    if nzeros == 0:
        print_board(board)
        exit()
    if board[row][col] == 0:
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            hr = row
            hc = col
            if iscorrect(board, row, col, i):
                board[row][col] = i
                if row == 8 and col == 8:
                    print_board(board)
                    exit()
                elif row == 8:
                    col += 1
                elif col == 8:
                    col = 0
                    row += 1
                else:
                    col += 1
                sudoku(board, nzeros - 1, row, col)
                nzeros += 1
                row = hr
                col = hc
                board[row][col] = 0
            else:
                continue
        return
    else:
        if row == 8 and col == 8:
            print_board(board)
            exit()
        elif row == 8:
            col += 1
        elif col == 8:
            col = 0
            row += 1
        else:
            col += 1
        sudoku(board, nzeros, row, col)
    return


if __name__ == "__main__":
    sudoku(board, num_zeros, 0, 0)
