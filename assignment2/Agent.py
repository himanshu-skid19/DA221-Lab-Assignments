
from TicTacToe import *


class Agent():
    def __init__(self, game):
        self.game = game
        self.player = game.current_player
        self.board = game.board

        self.opponent = "O" if self.player == "X" else "X"
    
    def evaluate_state(self, board):
        player = 0
        opponent = 0


        
        for i in range(3):
            if self.opponent not in board[i, :]:
                player+=1
            if self.player not in board[i, :]:
                opponent+=1
                    
            if self.opponent not in board[:, i]:
                player+=1
            if self.player not in board[:, i]:
                opponent+=1
                
        
            
        if self.opponent not in [board[0, 0], board[1, 1], board[2, 2]]:
                player+=1  
        if self.player not in [board[0, 0], board[1, 1], board[2, 2]]:
                opponent+=1      
        if self.opponent not in [board[0, 2], board[1, 1], board[2, 0]]:
                player+=1
        if self.player not in [board[0, 2], board[1, 1], board[2, 0]]:
                opponent+=1

        if self.game.check_winner(board) == "Winner: " + self.player:
            return float('inf')
        elif self.game.check_winner(board) == "Winner: " + self.opponent:
                return float('-inf')

                
        return player - opponent
    
    def is_terminal_state(self, board):
        for i in range(3):
            if board[i, 0] == board[i, 1] == board[i, 2] != "":
                return True
            if board[0, i] == board[1, i] == board[2, i] != "":
                return True
            if board[0, 0] == board[1, 1] == board[2, 2] != "":
                return True
            if board[0, 2] == board[1, 1] == board[2, 0] != "":
                return True
            if np.all(board != ""):
                return True
        return False
       

    def minimax(self, board, depth, alpha, beta, is_maximizing):
        if self.is_terminal_state(board) or depth == 9:
            evaluation = self.evaluate_state(board)
            return evaluation
        
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in self.game.get_available_moves():
                new_game = self.game.copy()
                new_game.make_move(move[0], move[1])
                eval = self.minimax(new_game.board, depth+1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                
            return max_eval
    
        else:
            min_eval = float('inf')
            for move in self.game.get_available_moves():
                 new_game = self.game.copy()
                 new_game.make_move(move[0], move[1])
                 eval = self.minimax(new_game.board, depth+1, alpha, beta, True)
                 min_eval = min(min_eval, eval)
                 beta = min(beta, eval)
                 if beta <= alpha:
                     break
            return min_eval        

    def make_best_move(self):
        best_score = float('-inf') if self.player == "X" else float('inf')
        best_move = None
        for move in self.game.get_available_moves():
            new_game = self.game.copy()
            new_game.make_move(move[0], move[1])
            score = self.minimax(new_game.board, 0, float('-inf'), float('inf'), False)
            if self.player == "X" and score > best_score:
                best_score = score
                best_move = move
            elif not self.player == "X" and score < best_score:            
                best_score = score
                best_move = move

        self.game.make_move(best_move[0], best_move[1])
    


