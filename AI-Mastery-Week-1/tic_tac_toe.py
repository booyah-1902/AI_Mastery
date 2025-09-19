#1 We need to print board after each input.
#   ---+---+---
#    1 | 2 | 3
#   ---+---+---
#    4 | 5 | 6
#   ---+---+---
#    7 | 8 | 9
#   ---+---+---
#2 Take in player input (1-9).
#3 Switch players and place their inputs on the board.
#4 Check if the game is won (player_1 or player_2), tied or ongoing by checking horizontal,vertical and diagonal winning patterns.
#5 Repeat 3 and 4 until the game has been won or tied. End game.

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












