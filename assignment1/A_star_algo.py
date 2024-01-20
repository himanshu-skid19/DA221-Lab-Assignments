import numpy as np

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal(self, state):
        if (state==self.goal_state).all():
            return True
        return False
    


    def get_successors(self, state):
        index = np.where(state == 0)
        moves = [(index[0][0]+ 1, index[1][0]), (index[0][0]-1, index[1][0]), (index[0][0], index[1][0]+1), (index[0][0], index[1][0] - 1)]
        legal_moves = []
        for i in moves:
            if (0 <= i[0] < state.shape[0]) and ((0 <= i[1] < state.shape[1])):
                legal_moves.append(i)
            continue

        successors = []
        for i in legal_moves:
            x = state.copy()
            x[index[0][0], index[1][0]] = x[i[0], i[1]]
            x[i[0], i[1]] = state[index[0][0], index[1][0]]
            successors.append(x)
        return successors
    

input = [8, 1, 2, 0, 4, 3, 7, 6, 5]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
input = np.array(input)
input = input.reshape(3,3)
goal = np.array(goal)
goal = goal.reshape(3,3)

x = Puzzle(input, goal)
y = x.get_successors(input)
for i in y:
    print(i)
    print()



    