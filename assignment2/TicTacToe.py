import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 1
        self.game_status = 'In progress'

    def initialize_board(self):
        return np.full((3, 3), -1)
    
    def display_board(self):
        print(self.board)

    def make_move(self, row, col):
        if self.board[row, col] == -1:
            self.board[row, col] = self.current_player
            self.current_player = 0 if self.current_player == 1 else 1
        else:
            print('Invalid move')

    def check_winner(self):
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != -1:
                self.game_status = 'Winner: ' + str(self.board[i, 0])
                return self.game_status
            if self.board[0, i] == self.board[1, i] == self.board[2, i] != -1:
                self.game_status = 'Winner: ' + str(self.board[i, 0])
                return self.game_status
            if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != -1:
                self.game_status = 'Winner: ' + str(self.board[i, 0])
                return self.game_status
            if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != -1:
                self.game_status = 'Winner: ' + str(self.board[i, 0])
                return self.game_status
            if np.all(self.board != -1):
                self.game_status = 'Draw'
                return self.game_status
            return self.game_status
        
    