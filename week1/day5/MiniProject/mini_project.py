# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.
# Here are the steps to implement the game:
# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).
# Step 2: Displaying the Game Board
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

# Step 3: Getting Player Input
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

# Step 4: Checking for a Winner
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

# Step 5: Checking for a Tie

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

# Step 6: The Main Game Loop

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def display_board(board):
    print("TIC TAC TOE:")
    print("*" * 11)
    for row in range(len(board)):
        line = "*" + " | ".join(board[row]) + "*"
        print(line)
        if row < 2:
            print("*" + "-" * 9 +"*")
        else:
            print("*" * 11)

def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_winner(board):
    ''' Check if there is a winner on the board '''
    for player in ["X", "O"]:
        if check_win(board, player):
            return player
    return None

def is_draw(board):
    ''' Check if the board is full and there is no winner  '''
    for row in board:
        if " " in row:
            return False
    return check_winner(board) is None

def play(): 
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        display_board(board)
        row = int(input(f"Player {current_player}, enter your move row (0-2): "))
        col = int(input(f"Player {current_player}, enter your move column (0-2): "))

        if (0 > row > 2) or (0 > col > 2) or board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    play()
    