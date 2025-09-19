#2 Human Players
# Board printed out each time (Matrix 1-9). 0 or X
#   ---+---+---
#    1 | 2 | 3
#   ---+---+---
#    4 | 5 | 6
#   ---+---+---
#    7 | 8 | 9
#   ---+---+---
#STEP 1 PLAYER 1 PICK 0 OR X
#STEP 2 ENTER (1-9) ON A MATRIX OF OPTIONS
#STEP 3 SWITCH PLAYER 7 REPEAT PROCESS
#STEP 4 AFTER 3 ENTRIES FROM PLAYER 1 CHECK HORIZONTAL, VERTICAL AND DIAGONAL TO SEE IF PLAYER HAS WON.
#STEP5 PLAYER WINS OR DRAWS. END GAME.

def init():
    choice = ""
    print("This is Tic-Tac-Toe")


    while choice != "O" and choice != "X":
        choice = input("Player 1, Choose either O or X:\n")
        if choice != "O" and choice != "X":
            print("You did not choose a from O or X")

    player_1 = choice

    if player_1 == "O" or player_1 == "X":
        if player_1 == "O":
            player_2 = "X"
            print("Player 1 is: O\nPlayer 2 is: X")
        else:
            player_2 = "O"
            print("Player 1 is: X\nPlayer 2 is: O")


def display(board):

        print("\n ---+---+---")
        print("  "+board[1] +' | ' + board[2] + ' | ' + board[3])
        print(" ---+---+---")
        print("  "+board[4] +' | ' + board[5] + ' | ' + board[6])
        print(" ---+---+---")
        print("  "+board[7] +' | ' + board[8] + ' | ' + board[9])
        print(" ---+---+---")

        coord = "\nPlayer 1, Choose a position between 1-9 to place your marker: "
        print(coord)

test_board = [None, '1', '2', '3', '4', '5', '6', '7', '8', '9']

init()
display(test_board)












