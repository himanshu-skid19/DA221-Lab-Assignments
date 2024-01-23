from solvability_check import *
from generate_instances import *
from A_star_algo import *


def main_menu():
    while True:
        choice = 0
        if choice == 0:
            print("\nWelcome! This is a program that showcases how to solve the 8-puzzle problem using A* Algorithm")
            print("1. Use your own input")
            print("2. Generate random examples")
            print("3. Try out other variations of the puzzle")
            print("4. Exit")

            choice = input("Enter your choice [1-4]: ")

            if choice == '1':
                inp = []
                goal = []
                print("Enter your input state of the puzzle in row major order:")
                for i in range(9):
                    x = int(input())
                    inp.append(x)

                inp = np.array(inp)
                inp = inp.reshape(3,3)
                print("Enter your goal state of the puzzle in row major order:")
                for i in range(9):
                    x = int(input())
                    goal.append(x)

                goal = np.array(goal)
                goal = goal.reshape(3,3)
                if not check_solvability(inp, 3):
                    print("This instance of the 8 puzzle is not solvable")
                else:
                    run_algo(inp, goal)
                choice = 0
                
                
            elif choice == '2':
                print("Generating 10 instances of 8 puzzle as specified by the assigment which are given as follows: ")
                instances = generate_instances(3, 10)
                for i in instances:
                    print(i)
                    print()
                
                c = 0
                goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                goal = np.array(goal)
                goal = goal.reshape(3,3)

                print("The goal state is given by: \n", goal)

                if c==0:
                    print("\nWhich heuristic function do you want to use to run the A* algorithm?")
                    print("1. Hamming Priority")
                    print("2. Manhattan Distance")
                    print("3. Manhattan with Linear Conflict")
                    print("4. Back")

                    c= int(input("Enter your choice [1-4]: "))
                    if c == 1:
                        for i in instances:
                            puzz = Puzzle(i, goal)
                            t, p, l, n = puzz.run_hamming()
                            print(i)
                            print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\n")
                    if c == 2:
                        for i in instances:
                            puzz = Puzzle(i, goal)
                            t, p, l, n = puzz.run_manhattan()
                            print(i)
                            print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\n")
                    if c == 3:
                        for i in instances:
                            puzz = Puzzle(i, goal)
                            t, p, l, n = puzz.run_manhattan_linear()
                            print(i)
                            print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\n")
                    if c == 0:
                        choice = 0
                


                

            elif choice == '3':
                print("Disclaimer: Some examples can take a long time to run especially in python, so be mindful of that")
                c = 0
                if c == 0:
                    n = int(input("Enter the size of n (nxn)"))
                    print("\nWelcome! This is a program that showcases how to solve the 8-puzzle problem using A* Algorithm")
                    print("1. Use your own input")
                    print("2. Generate random examples")
                    print("3. Back")

                    c = int(input("Enter your choice [1-4]: "))

                    if c == 1:
                        inp = []
                        goal = []
                        print("Enter your input state of the puzzle in row major order:")
                        for i in range(n):
                            x = int(input())
                            inp.append(x)

                        inp = np.array(inp)
                        inp = inp.reshape(n,n)
                        print("Enter your goal state of the puzzle in row major order:")
                        for i in range(n):
                            x = int(input())
                            goal.append(x)

                        goal = np.array(goal)
                        goal = goal.reshape(n,n)
                        if not check_solvability(inp, n):
                            print(f"This instance of the {n*n-1} puzzle is not solvable")
                        else:
                            run_algo(inp, goal)
                        choice = 0

                    if c==2:
                        m = int(input("How many examples do you want to generate? "))
                        instances = generate_instances(n, m)
                        for i in instances:
                            print(i)
                            print()
                        
                        c1 = 0
                        goal = [i for i in range(n*n)]
                        goal = np.array(goal)
                        goal = goal.reshape(n,n)

                        print("The goal state is given by: \n", goal)

                        if c1==0:
                            print("\nWhich heuristic function do you want to use to run the A* algorithm?")
                            print("1. Hamming Priority")
                            print("2. Manhattan Distance")
                            print("3. Manhattan with Linear Conflict")
                            print("4. Back")

                            c1= int(input("Enter your choice [1-4]: "))
                            if c1 == 1:
                                for i in instances:
                                    puzz = Puzzle(i, goal)
                                    t, p, l, n1 = puzz.run_hamming()
                                    print(i)
                                    print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n1}\n")
                            if c1 == 2:
                                for i in instances:
                                    puzz = Puzzle(i, goal)
                                    t, p, l, n1= puzz.run_manhattan()
                                    print(i)
                                    print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n1}\n")
                            if c1 == 3:
                                for i in instances:
                                    puzz = Puzzle(i, goal)
                                    t, p, l, n1 = puzz.run_manhattan_linear()
                                    print(i)
                                    print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n1}\n")
                            if c1 == 4:
                                c = 0




            
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose [1-4].")

if __name__ == "__main__":
    main_menu()