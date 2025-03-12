# Tic Tac Toe Game in Python
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_win(board, player):
    win_conditions = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # middle column
        [2, 5, 8],  # right column
        [0, 4, 8],  # diagonal from top-left
        [2, 4, 6],  # diagonal from top-right
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_tie(board):
    return all(space in ["X", "O"] for space in board)


def tic_tac_toe():
    # Initialize the board with position numbers 1 to 9
    # board = [str(i + 1) for i in range(9)]
    # or an empty board
    board = [" "] * 9  # Create an empty board
    current_player = "X"  # X starts the game

    while True:
        display_board(board)

        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            if board[move] in ["X", "O"]:
                print("That position is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # Update the board with the current player's move
        board[move] = current_player

        # Check for a win
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


# Run the game
tic_tac_toe()
