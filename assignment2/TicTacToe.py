import numpy as np
class TicTacToe:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "X"
        self.game_status = 'In progress'

    def initialize_board(self):
        return np.full((3, 3), "")
    
    def display_board(self):
        print(self.board)

    def make_move(self, row, col):
        if self.board[row, col] == "":
            self.board[row, col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print('Invalid move')

    def get_available_moves(self):
        return np.argwhere(self.board == "")
    
    def check_winner(self, board):
        for i in range(3):
            if board[i, 0] == board[i, 1] == board[i, 2] != "":
                self.game_status = 'Winner: ' + str(board[i, 0])
                return self.game_status
            if board[0, i] == board[1, i] == board[2, i] != "":
                self.game_status = 'Winner: ' + str(board[0, 1])
                return self.game_status
            if board[0, 0] == board[1, 1] == board[2, 2] != "":
                self.game_status = 'Winner: ' + str(board[1, 1])
                return self.game_status
            if board[0, 2] == board[1, 1] == board[2, 0] != "":
                self.game_status = 'Winner: ' + str(board[1, 1])
                return self.game_status
            if np.all(board != ""):
                self.game_status = 'Draw'
                return self.game_status
            return self.game_status

    def copy(self):
        new_game = TicTacToe()
        new_game.board = self.board.copy()
        new_game.current_player = self.current_player
        new_game.game_status = self.game_status
        return new_game
        