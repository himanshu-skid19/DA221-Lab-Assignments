from minimax_agent import *

def test_winning_condition_for_x():
    game = TicTacToe_Agent()
    board_state = [
        ['X', 'X', 'O'],
        ['O', 'X', None],
        ['O', None, None]
    ]


    game.set_board(board_state)
    assert game.check_winner(game.board, 'X') == False, "X should not be a winner yet."
    ai_move = game.get_ai_move()
    # print(ai_move)
    board = game.make_move(game.board, ai_move, 'X')
    assert game.check_winner(board, 'X') == True, "X should be a winner now."

def test_blocking_move():
    game = TicTacToe_Agent()
    board_state = [
        ['X', 'O', 'X'],
        ['O', None, None],
        [None, None, None]
    ]
    game.set_board(board_state)
    ai_move = game.get_ai_move(False)  # Assuming 'O' is the AI here
    assert ai_move == (1, 1) or ai_move == (1, 2), "AI should block 'X' from winning."

def test_draw_condition():
    game = TicTacToe_Agent()
    board_state = [
        ['X', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', 'X', None]
    ]
    game.set_board(board_state)
    ai_move = game.get_ai_move(False)  # Assuming 'O' is the AI here
    board = game.make_move(game.board, ai_move, 'O')
    assert game.is_terminal_state(board) == True, "The game should be in a terminal state."
    assert game.check_winner(board, 'X') == False, "X should not win."
    assert game.check_winner(board, 'O') == False, "O should not win."
    assert game.get_legal_moves(board) == [], "There should be no legal moves left."

def test(board_state, expected_move):
    game = TicTacToe_Agent()
    game.set_board(board_state)
    ai_move = game.get_ai_move(False)  # Assuming 'O' is the AI here
    print(ai_move)
    assert ai_move == expected_move, "AI should make the correct move."


def test_evaluation():
    game = TicTacToe_Agent()
    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    game.set_board(board_state)
    assert game.evaluate_state(game.board) == 0, "The board should be a draw."

    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', None]
    ]
    game.set_board(board_state)
    assert game.evaluate_state(game.board) == 0, "The board should be a draw."

    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', None, 'X']
    ]
    game.set_board(board_state)
    assert game.evaluate_state(game.board) == -1, "The board should be a win for 'O'."

    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        [None, 'X', 'X']
    ]
    game.set_board(board_state)

    assert game.evaluate_state(game.board) == 2, "The board should be a win for 'X'."

    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        [None, None, 'X']
    ]
    game.set_board(board_state)
    assert game.evaluate_state(game.board) == 1, "The board should be a draw."

    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        [None, 'X', None]
    ]
    game.set_board(board_state)
    assert game.evaluate_state(game.board) == 2, "The board should be a draw."

    board_state = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['X', None, None]
    ]
    game.set_board(board_state)
    assert game.evaluate_state(game.board) == math.inf, "X won the game."



test_winning_condition_for_x()
test_blocking_move()
test_draw_condition()
test_evaluation()
