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

def display_board(board):
    """Display the tic-tac-toe board"""
    print("\n ---+---+---")
    print("  " + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(" ---+---+---")
    print("  " + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(" ---+---+---")
    print("  " + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(" ---+---+---")


def get_valid_position(player_name, board):
    """Get a valid position from the player with full validation"""
    while True:
        try:
            position = int(input(f"\n{player_name}, choose a position from 1-9: "))
            
            # Check if number is in valid range
            if position not in range(1, 10):
                print("Please choose a number between 1 and 9")
                continue
            
            # Check if position is already taken
            if board[position] in ['X', 'O']:
                print("That position is already taken! Choose another.")
                continue
                
            # If we get here, the input is valid
            return position
            
        except ValueError:
            print("Please enter a number")


def get_player_symbols():
    """Get player symbol choices (X or O)"""
    print("This is Tic-Tac-Toe")
    
    while True:
        choice = input("Player 1, choose either O or X: ").upper()
        if choice in ['O', 'X']:
            player_1 = choice
            player_2 = 'X' if choice == 'O' else 'O'
            print(f"Player 1 is: {player_1}")
            print(f"Player 2 is: {player_2}")
            return player_1, player_2
        else:
            print("Please choose either O or X")


def main():
    # Initialize the board
    board = [None, '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Get player symbols
    player_1, player_2 = get_player_symbols()
    
    # Show initial board
    display_board(board)
    
    # Main game loop
    while True:
        # Player 1's turn
        position = get_valid_position("Player 1", board)
        board[position] = player_1
        display_board(board)
        
        # TODO: Check for win or draw here
        
        # Player 2's turn  
        position = get_valid_position("Player 2", board)
        board[position] = player_2
        display_board(board)
        
        # TODO: Check for win or draw here


# Run the game
if __name__ == "__main__":
    main()