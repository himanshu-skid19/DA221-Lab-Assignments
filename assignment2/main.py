from TicTacToe import *
from Agent import *

game = TicTacToe()
agent = Agent(game)

# game.display_board()
# game.check_winner()

# while (game.check_winner(game.board) == 'In progress'):
#     if game.current_player == 'X':
#         game.display_board()
#         row = int(input('Enter row: '))
#         col = int(input('Enter col: '))
#         game.make_move(row, col)
#     else:
#         agent.make_best_move()

# print(game.check_winner(game.board))

x = np.asarray([['', 'O', 'O'], ['', 'X', 'X'], ['X', '', '']])
print(agent.evaluate_state(x))