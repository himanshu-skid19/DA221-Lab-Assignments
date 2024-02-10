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
    
    def check_winner(self):
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != "":
                self.game_status = 'Winner: ' + str(self.board[i, 0])
                return self.game_status
            if self.board[0, i] == self.board[1, i] == self.board[2, i] != "":
                self.game_status = 'Winner: ' + str(self.board[i, 0])
                return self.game_status
            if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != "":
                self.game_status = 'Winner: ' + str(self.board[1, 1])
                return self.game_status
            if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != "":
                self.game_status = 'Winner: ' + str(self.board[1, 1])
                return self.game_status
            if np.all(self.board != ""):
                self.game_status = 'Draw'
                return self.game_status
            return self.game_status

    def copy(self):
        new_game = TicTacToe()
        new_game.board = self.board.copy()
        new_game.current_player = self.current_player
        new_game.game_status = self.game_status
        return new_game
        



class Agent():
    def __init__(self, game):
        self.game = game
        self.player = game.current_player
        self.board = game.board

        self.opponent = "O" if self.player == "X" else "X"
    
    def evaluate_state(self, board):
        player = 0
        opponent = 0

        if np.all(board != ""):
            player = 8
            opponent = 8
            return 0
        for i in range(3):
            if self.opponent not in [board[i, 0], board[i, 1], board[i, 2]]:
                player+=1
            if self.player not in [board[i, 0], board[i, 1], board[i, 2]]:
                opponent+=1
                    
            if self.opponent not in [board[0, i], board[1, i], board[2, i]]:
                player+=1
            if self.player not in [board[i, 0], board[i, 1], board[i, 2]]:
                opponent+=1
                
        
            
        if self.opponent not in [board[0, 0], board[1, 1], board[2, 2]]:
                player+=1  
        if self.player not in [board[0, 0], board[1, 1], board[2, 2]]:
                opponent+=1      
        if self.opponent not in [board[0, 2], board[1, 1], board[2, 0]]:
                player+=1
        if self.player not in [board[0, 2], board[1, 1], board[2, 0]]:
                opponent+=1
        

                
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
            return self.evaluate_state(board)
        
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
    



game = TicTacToe()
agent = Agent(game)

# game.display_board()
# game.check_winner()

while (game.check_winner() == 'In progress'):
    if game.current_player == 'X':
        game.display_board()
        row = int(input('Enter row: '))
        col = int(input('Enter col: '))
        game.make_move(row, col)
    else:
        agent.make_best_move()

print(game.check_winner())
