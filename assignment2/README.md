# Play TicTacToe with Minimax Agent
This program is a simple implementation of the game TicTacToe. The game is played between a human and an AI agent. The AI agent uses the Minimax algorithm to make its moves. The game is played in the terminal. Moreover, i have implemented alpha-beta pruning to optimize the minimax algorithm.

This program is part ofthe assignment 2 of the course "Introduction to Artificial Intelligence" at Indian Institute of Technology, Guwahati.

## How to run the program
To run the program, simply run the following command in the terminal:
```bash
python main.py
```
Note: Make sure you have python installed in your system.

## How to play the game
Running the program will give you following options"
1. Play as X
2. Play as O

Choose the option you want to play as. Then, the game will start and you will be asked to make your move. The board is numbered as follows:
```bash
0 0 | 0 1 | 0 2
---------------
1 0 | 1 1 | 1 2
---------------
2 0 | 2 1 | 2 2
```
Enter the row and column number where you want to make your move. The game will continue until one of the players wins or the game ends in a draw.

## Test Cases
The test cases for the program are present in the file test_agent.py. To run the test cases, simply run the following command in the terminal:
```bash
python test_agent.py
```
If the program runs without any errors, it mean it passed all the tests.

### Creating your own test cases
You can create your own test cases by adding new test functions in the file test_agent.py. The test functions should start with the word "test". The test functions should use the assert statement to check if the output of the function is as expected.

Example:
```python
def test_winning_condition_for_x():
    game = TicTacToe_Agent()
    board_state = [
        ['X', 'X', 'O'],
        ['O', 'X', None],
        ['O', None, None]
    ]


    game.set_board(board_state)
    assert game.check_winner(game.board, 'X') == False, "X should not be a winner yet."
    depth = 8
    ai_move, n = game.get_ai_move(depth)
    board = game.make_move(game.board, ai_move, 'X')
    assert game.check_winner(board, 'X') == True, "X should be a winner now."
```
In the above example, the test function checks if the function check_winner is working correctly or not. The function checks if the player 'X' has won the game or not. The function creates a board state and then checks if the player 'X' has won the game or not. If the player has won, the function will pass the test, otherwise it will fail.

To modify this, you can use your own board state and check if the player has won the game or not, or any other scenario you want to test. You will have to change the assert statement accordingly. Also you can modify the depth of the minimax algorithm to check for different scenarios.

## Author
```bash
Himanshu Singhal
220150004
IIT Guwahati
```


