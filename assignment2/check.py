import math

PLAYER_MAX = 'X'
PLAYER_MIN = 'O'
EMPTY = None

def count_open_directions(board, player):
    count = 0
    size = len(board)
    opponent = 'O' if player == 'X' else 'X'

    # Check rows and columns
    for i in range(size):
        if opponent not in board[i]:  # Check row
            count += 1
        if opponent not in [board[j][i] for j in range(size)]:  # Check column
            count += 1

    # Check diagonals
    if opponent not in [board[i][i] for i in range(size)]:  # Check main diagonal
        count += 1
    if opponent not in [board[i][size - i - 1] for i in range(size)]:  # Check anti-diagonal
        count += 1

    return count

def check_winner(board, player):
    size = len(board)
    
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True

    # Check main diagonal
    if all(board[i][i] == player for i in range(size)):
        return True

    # Check anti-diagonal
    if all(board[i][size - i - 1] == player for i in range(size)):
        return True

    return False

def evaluate_state(board):
    if check_winner(board, PLAYER_MAX):
        return math.inf
    elif check_winner(board, PLAYER_MIN):
        return -math.inf
    else:
        return count_open_directions(board, PLAYER_MAX) - count_open_directions(board, PLAYER_MIN)
    

def is_terminal_state(board):
    return check_winner(board, PLAYER_MAX) or check_winner(board, PLAYER_MIN) or not any(EMPTY in row for row in board)

def get_legal_moves(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == EMPTY]

def make_move(board, move, player):
    new_board = [row[:] for row in board]
    new_board[move[0]][move[1]] = player
    return new_board

def minimax(board, depth, is_maximising):
    if is_terminal_state(board) or depth == 0:
        return evaluate_state(board), None
    
    if is_maximising:
        max_eval = -math.inf
        best_move = None
        for move in get_legal_moves(board):
            value, _ = minimax(make_move(board, move, PLAYER_MAX), depth - 1, False)
            if value >= max_eval:
                max_eval = value
                best_move = move
        return max_eval, best_move
    
    else:
        min_eval = math.inf
        best_move = None
        for move in get_legal_moves(board):
            value, _ = minimax(make_move(board, move, PLAYER_MIN), depth - 1, True)
            if value <= min_eval:
                min_eval = value
                best_move = move
        return min_eval, best_move
    
def display_board(board):
        for row in board:
            print(' | '.join([cell if cell is not None else ' ' for cell in row]))
            print('----------')


# board = [
#     ['X', 'O', 'X'],
#     [EMPTY, 'X', EMPTY],
#     ['O', EMPTY, 'O']
# ]


# value, best_move = minimax(board, depth=5, is_maximising=False)
# print(f"Best value: {value}, Best move: {best_move}")

board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]


current_player = PLAYER_MAX   
while (check_winner(board, PLAYER_MAX) or check_winner(board, PLAYER_MIN)) == False:
    display_board(board)
    if (is_terminal_state(board)):
        print("Game Over")
        break
    
    if (current_player == PLAYER_MAX):
        print("Player's turn")
        print()
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        board = make_move(board, (row, col), PLAYER_MAX)
        current_player = PLAYER_MIN
    else:
        print("Agent's turn")
        print()
        value, best_move = minimax(board, depth=9, is_maximising=False)
        board = make_move(board, best_move, PLAYER_MIN)
        current_player = PLAYER_MAX
    
display_board(board)

