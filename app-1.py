import streamlit as st

# Initialize session state variables for Tic Tac Toe
if 'board' not in st.session_state:
    st.session_state.board = [' ' for _ in range(9)]
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'X'
if 'winner' not in st.session_state:
    st.session_state.winner = None

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
computer = 'X'

def check_winner(board):
    # Check all winning combinations
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

def check_draw(board):
    return all(space != ' ' for space in board)

def make_move(index):
    if st.session_state.board[index] == ' ' and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.board)
        
        if st.session_state.winner:
            st.success(f"{st.session_state.winner} wins!")
        elif check_draw(st.session_state.board):
            st.info("It's a draw!")
        else:
            # Switch players
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

def reset_game():
    st.session_state.board = [' ' for _ in range(9)]
    st.session_state.current_player = 'X'
    st.session_state.winner = None

# Streamlit layout
st.title("Tic Tac Toe")
st.write(f"Current Player: {st.session_state.current_player}")

# Create a 3x3 grid of buttons
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        index = row * 3 + col
        if cols[col].button(st.session_state.board[index], key=index):
            make_move(index)

# Reset button
if st.button("Reset Game"):
    reset_game()
