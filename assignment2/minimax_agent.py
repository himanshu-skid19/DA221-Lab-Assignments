import math

class TicTacToe_Agent:
    def __init__(self):
        self.PLAYER_MAX = 'X'
        self.PLAYER_MIN = 'O'
        self.EMPTY = None
        self.board = [[self.EMPTY for _ in range(3)] for _ in range(3)]


    def set_board(self, board):
        self.board = board

    def get_ai_move(self, is_maximising=True):
        _, move = self.minimax(self.board, 9, is_maximising)
        return move
    
    def get_ai_move_alpha_beta(self, is_maximising=True):
        _, move = self.minimax_with_alpha_beta_pruning(self.board, 9, -math.inf, math.inf, is_maximising)
        return move
    
    def choose_starting_player(self):
        player_choice = input("Choose the starting player - 'X' for you or 'O' for AI: ").strip().upper()
        if player_choice == 'X':
            return self.PLAYER_MAX
        elif player_choice == 'O':
            return self.PLAYER_MIN
        else:
            print("Invalid choice. Defaulting to 'X' starting.")
            return self.PLAYER_MAX

    def count_open_directions(self, board, player):
        count = 0
        size = len(board)
        opponent = 'O' if player == 'X' else 'X'

        # Check rows and columns
        for i in range(size):
            if opponent not in board[i]:  # Check row
                count += 1  # Count open row

            if opponent not in [board[j][i] for j in range(size)]:  # Check column
                count += 1
        
        # Check diagonals
        if opponent not in [board[i][i] for i in range(size)]:
            count += 1
        if opponent not in [board[i][size - i - 1] for i in range(size)]:
            count += 1

        return count
    
    def check_winner(self, board, player):
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
    
    def evaluate_state(self, board):
        f = self.count_open_directions(board, self.PLAYER_MAX) - self.count_open_directions(board, self.PLAYER_MIN)
        if self.check_winner(board, self.PLAYER_MAX):
            return math.inf
        elif self.check_winner(board, self.PLAYER_MIN):
            return -math.inf
        else:
            return f
        
    def is_terminal_state(self, board): 
        return self.check_winner(board, self.PLAYER_MAX) or self.check_winner(board, self.PLAYER_MIN) or not any(self.EMPTY in row for row in board)

    def display_board(self, board):
        for row in board:
            print(' | '.join([cell if cell is not None else ' ' for cell in row]))
            print('----------')

    def get_legal_moves(self, board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == self.EMPTY]
    
    def make_move(self, board, move, player):
        """
        Apply a move to the board for a given player and return the new board state.
        
        :param board: The current board state.
        :param move: A tuple (row, col) indicating the move's position.
        :param player: The player ('X' or 'O') making the move.
        :return: A new board state with the move applied.
        """
        # Create a deep copy of the board to avoid mutating the original board
        new_board = [row[:] for row in board]
        
        # Apply the move
        new_board[move[0]][move[1]] = player
        
        return new_board

    def minimax(self, board,  depth, is_maximising):
        if self.is_terminal_state(board) or depth == 0:
            return self.evaluate_state(board), None

        if is_maximising:
            best_value = -math.inf
            best_move = None
            for move in self.get_legal_moves(board):
                new_board = self.make_move(board, move, self.PLAYER_MAX)
                value, _ = self.minimax(new_board, depth - 1, False)
                if value >= best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = math.inf
            best_move = None
            for move in self.get_legal_moves(board):
                new_board = self.make_move(board, move, self.PLAYER_MIN)
                value, _ = self.minimax(new_board, depth - 1, True)
                if value <= best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        
    def minimax_with_alpha_beta_pruning(self, board, depth, alpha, beta, is_maximising):
        if self.is_terminal_state(board) or depth == 0:
            return self.evaluate_state(board), None

        if is_maximising:
            best_value = -math.inf
            best_move = None
            for move in self.get_legal_moves(board):
                new_board = self.make_move(board, move, self.PLAYER_MAX)
                value, _ = self.minimax_with_alpha_beta_pruning(new_board, depth - 1, alpha, beta, False)
                if value >= best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value, best_move
        else:
            best_value = math.inf
            best_move = None
            for move in self.get_legal_moves(board):
                new_board = self.make_move(board, move, self.PLAYER_MIN)
                value, _ = self.minimax_with_alpha_beta_pruning(new_board, depth - 1, alpha, beta, True)
                if value <= best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value, best_move
        
    def play(self):
        depth = int(input("Enter the depth for the Minimax algorithm: "))

        current_board = self.board  # Initial board state
        current_player = self.choose_starting_player() # Human player starts

        while not self.is_terminal_state(current_board):
            self.display_board(current_board)
            if current_player == self.PLAYER_MAX:
                move = None
                while move is None:
                    try:
                        row, col = map(int, input('Enter row and column (0-2, space-separated): ').split())
                        if (0 <= row <= 2 and 0 <= col <= 2) and current_board[row][col] == self.EMPTY:
                            current_board = self.make_move(current_board, (row, col), self.PLAYER_MAX)
                            move = (row, col)  # Successfully made a move
                        else:
                            print('Invalid move. Try again.')
                    except ValueError:
                        print('Please enter valid row and column numbers.')
                current_player = self.PLAYER_MIN
            else:
                print("AI's turn...")
                _, move = self.minimax(current_board, depth, False)  # Assuming depth 9 for full game tree search
                if move:
                    current_board = self.make_move(current_board, move, self.PLAYER_MIN)
                    current_player = self.PLAYER_MAX
                else:
                    print("No valid moves left. It's a draw.")
                    break

            if self.check_winner(current_board, self.PLAYER_MIN):
                self.display_board(current_board)
                print('AI wins!')
                break
            elif self.check_winner(current_board, self.PLAYER_MAX):
                self.display_board(current_board)
                print('Congratulations, you win!')
                break
            elif not self.get_legal_moves(current_board):
                self.display_board(current_board)
                print('The game is a draw.')
                break

        if not any([self.check_winner(current_board, self.PLAYER_MAX), self.check_winner(current_board, self.PLAYER_MIN), self.get_legal_moves(current_board)]):
            self.display_board(current_board)
            print("It's a draw!")


    def play_with_alpha_beta_pruning(self):

        depth = int(input("Enter the depth for the Minimax algorithm: "))
        current_board = self.board  # Initial board state
        current_player = self.choose_starting_player()
        while not self.is_terminal_state(current_board):
            self.display_board(current_board)
            if current_player == self.PLAYER_MAX:
                move = None
                while move is None:
                    try:
                        row, col = map(int, input('Enter row and column (0-2, space-separated): ').split())
                        if (0 <= row <= 2 and 0 <= col <= 2) and current_board[row][col] == self.EMPTY:
                            current_board = self.make_move(current_board, (row, col), self.PLAYER_MAX)
                            move = (row, col)  # Successfully made a move
                        else:
                            print('Invalid move. Try again.') 
                    except ValueError:
                        print('Please enter valid row and column numbers.')
                current_player = self.PLAYER_MIN
            else:
                print("AI's turn...")
                _, move = self.minimax_with_alpha_beta_pruning(current_board, depth, -math.inf, math.inf, False)
                if move:
                    current_board = self.make_move(current_board, move, self.PLAYER_MIN)
                    current_player = self.PLAYER_MAX
                else:
                    print("No valid moves left. It's a draw.")
                    break

            if self.check_winner(current_board, self.PLAYER_MIN):
                self.display_board(current_board)
                print('AI wins!')
                break
            elif self.check_winner(current_board, self.PLAYER_MAX):
                self.display_board(current_board)
                print('Congratulations, you win!')
                break
            elif not self.get_legal_moves(current_board):
                self.display_board(current_board)
                print('The game is a draw.')
                break

        if not any([self.check_winner(current_board, self.PLAYER_MAX), self.check_winner(current_board, self.PLAYER_MIN), self.get_legal_moves(current_board)]):
            self.display_board(current_board)
            print("It's a draw!")



# if __name__ == '__main__':
#     game = TicTacToe_Agent()
#     # game.play()
#     game.play_with_alpha_beta_pruning( )
    