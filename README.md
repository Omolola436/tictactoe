Tic Tac Toe Game with Streamlit
Welcome to the Tic Tac Toe Game! This app allows users to play a simple Tic Tac Toe game with an intuitive interface built using Streamlit.

Table of Contents
Installation
How to Play
Code Overview
Usage
Features
Installation
To run this game, you need Python and Streamlit installed. You can install Streamlit using pip:

pip install streamlit
How to Play
Start the game: Run the app, and a 3x3 grid will appear with the message indicating which player’s turn it is.
Make a Move: Click on any empty cell in the grid to make a move.
The game alternates between players 'X' and 'O'.
Winning or Draw:
The game checks for a win condition after each move.
If all cells are filled without a winner, the game declares a draw.
Reset the Game: Click the "Reset Game" button to restart the game.
Code Overview
Session State Variables
st.session_state.board: Stores the current state of the Tic Tac Toe board as a list of 9 elements, initialized as empty spaces (' ').
st.session_state.current_player: Keeps track of the current player, initialized as 'X'.
st.session_state.winner: Indicates if there’s a winner (set to None initially).
Functions
check_winner(board): Checks for a winning condition by evaluating the rows, columns, and diagonals of the board.
check_draw(board): Checks if all cells are filled without a winner.
make_move(index): Updates the board with the current player's move and checks for a winner or a draw. It switches the current player if the game is ongoing.
reset_game(): Resets the game state, initializing the board, setting the current player to 'X', and clearing the winner.
Streamlit Layout
Title: Displays "Tic Tac Toe" at the top.
Current Player Display: Shows which player's turn is up.
3x3 Grid: Uses Streamlit columns to display the Tic Tac Toe board and allow user interaction.
Reset Button: Allows players to reset the game at any time.
Usage
To run the game:


streamlit run <filename>.py
Replace <filename>.py with the name of the Python file containing the code.

Features
Interactive Gameplay: Users can click cells to make moves.
Automatic Win/Draw Detection: The app instantly notifies users of a win or draw condition.
Game Reset: Allows players to restart the game with the click of a button.
