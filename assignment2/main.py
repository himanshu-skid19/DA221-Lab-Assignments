from minimax_agent import *
from test_agent import *

def main_menu():
    print("Welcome to my implementation of the Minimax Algorithm on the game of TicTacToe!")
    print("1. Play against the AI")
    print("2. Exit")

    choice = input("Enter your choice [1-2]: ")

    if choice == '1':        
        a = -1
        game = TicTacToe_Agent()
        while a==-1:
            print("Which verson of the agent do you want to play against? ")
            print("1. Minimax Agent")
            print("2. Alpha-Beta Pruning Agent")
            a = int(input("Enter your choice [1-2]: "))
            if a==1:
                a = 0
            elif a==2:
                a = 1
            else:
                print("Invalid choice. Please choose [1-2].")
                a = -1
        
        if a==1:
            game.play_with_alpha_beta_pruning()

        else:
            game.play()  
            

    elif choice == '2':
        print("Exiting the program.")
    else:
        print("Invalid choice. Please choose [1-3].")



if __name__ == "__main__":
    main_menu()