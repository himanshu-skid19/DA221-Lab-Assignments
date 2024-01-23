from solvability_check import *
from numpy import random
from A_star_algo import *

n = 9

def generate_instances(n, num_examples):
    possibilites = [i for i in range(n*n)]

    instances = []

    while (len(instances)<num_examples):
        trial = possibilites.copy()
        random.shuffle(trial)
        trial = np.array(trial)
        trial = trial.reshape(n,n)
        if (check_solvability(trial, n)):
            instances.append(trial)
        else:
            continue
        pass

    return instances



def run_algo(initial_state, final_state):
    puzz = Puzzle(initial_state, final_state)
    while True:
        choice = 0
        if choice == 0:
            print("\nWhich heuristic function do you want to use to run the A* algorithm?")
            print("1. Hamming Priority")
            print("2. Manhattan Distance")
            print("3. Manhattan with Linear Conflict")
            print("4. Back")

            choice = int(input("Enter your choice [1-4]: "))

            if choice == 1:
                t, p, l, n = puzz.run_hamming()
                print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\n")
                print("Would you like to view the entire path to the solution?")
                while True:
                    ans = input("Y/N")
                    if ans in ["Y", "y", "N", "n"]:
                        break
                if ans in ["Y", "y"]:
                    print("Path:\n", p)
                choice = 0


            if choice == 2:
                t, p, l, n = puzz.run_manhattan()
                print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\n")
                print("Would you like to view the entire path to the solution?")
                while True:
                    ans = input("Y/N")
                    if ans in ["Y", "y", "N", "n"]:
                        break
                if ans in ["Y", "y"]:
                    print("Path:\n", p)
                choice = 0
                    
            if choice == 3:
                t, p, l, n = puzz.run_manhattan_linear()
                print(f"Time taken: {t}\n Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\n")
                print("Would you like to view the entire path to the solution?")
                while True:
                    ans = input("Y/N")
                    if ans in ["Y", "y", "N", "n"]:
                        break
                if ans in ["Y", "y"]:
                    print("Path:\n", p)
                choice = 0

            if choice == 4:
                break
    return 0



