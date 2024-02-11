from minimax_agent import *
import time
import random

random.seed(0)


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

def test(boards, pruning=False):
    game = TicTacToe_Agent()
    
    total_time = 0
    total_nodes = 0
    if (pruning):
        for i in boards:
            game.set_board(i)
            t1 = time.time()
            ai_move, n = game.get_ai_move_alpha_beta(False)
            t2 = time.time()
            total_time += (t2-t1)*1e6
            total_nodes += n
    else:
        for i in boards:
            game.set_board(i)
            t1 = time.time()
            ai_move, n = game.get_ai_move(False)
            t2 = time.time()
            total_time += (t2-t1)*1e6
            total_nodes += n
    return total_time/len(boards), total_nodes/len(boards)



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



# test_winning_condition_for_x()
# test_blocking_move()
# test_draw_condition()
# test_evaluation()

boards = [[
        [None, 'X', 'O'],
        [None, None, None],
        ['O', None, None]
    ], [
        ['X', 'O', 'X'],
        ['X', None, 'O'],
        ['X', None, None]
    ],
    [
        ['X', None, 'X'],
        ['X', 'O', 'O'],
        [None, 'X', None]
    ],
    [
        ['X', 'O', None],
        ['X', 'O', 'O'],
        [None, None, None]
    ],
    [
        ['X', None, 'X'],
        [None, None, 'O'],
        ['O', None, 'X']
    ],
    [
        [None, 'O', 'X'],
        [None, 'O', 'O'],
        [None, 'X', None]
    ],
    [
        ['X', 'O', None],
        ['X', None, 'O'],
        [None, None, 'X']
    ],
    [
        ['X', None, 'X'],
        ['X', None, 'O'],
        [None, None, None]
    ],
    [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['X', None, None]
    ],
    [
        ['X', None, 'X'],
        [None, None, 'O'],
        [None, None, None]
    ],
    [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        [None, None, 'X']
    ],
    [
        [None, None, 'X'],
        [None, 'O', 'O'],
        ['X', None, 'X']
    ],
    [
        [None, 'O', 'X'],
        ['X', 'O', 'O'],
        [None, 'X', None]
    ],
    [
        ['X', None, None],
        [None, None, None],
        [None, None, None]
    ],
    [
        [None, 'X', None],
        ['X', None, 'O'],
        [None, None, None]
    ]
  
    
    ]

t1, n1 = test(boards, True)
print("Average time taken for Minimax with Alpha-Beta Pruning: ", t1, "ms")
print("Average number of nodes evaluated: ", int(n1))
t2, n2 = test(boards, False)
print("Average time taken for Minimax without Alpha Beta Pruning: ", t2, "ms")
print("Average number of nodes evaluated: ", int(n2))


# game = TicTacToe_Agent()
# board_state = [
#         ['X', 'O', 'X'],
#         ['O', None, None],
#         [None, None, None]
#     ]


# for i in boards:
#     game.set_board(i)
#     ai_move, n = game.get_ai_move(False)
#     print(ai_move)
#     ai_move, m = game.get_ai_move_alpha_beta(False)    
#     print(m)
#     print(n)
#     print("\n")


# # game.set_board(board_state)
# # ai , m = game.get_ai_move(False)
# # ai_move, n = game.get_ai_move_alpha_beta(False)
# # print(n)
# # print(m)