from TicTacToe import *
from Agent import *

game = TicTacToe()

game.display_board()
game.make_move(0, 0)
game.make_move(0, 1)
game.make_move(1, 1)
game.make_move(0, 2)
game.make_move(2, 2)


print(game.check_winner())
game.display_board()