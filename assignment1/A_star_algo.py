import numpy as np
from queue import PriorityQueue
import timeit

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.length = 0
        self.state_id_counter = 0

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
    
    def hamming_priority(self, state):
        count = 0
        # print(state)
        
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    continue
                if state[i][j] != self.goal_state[i][j]:
                    count +=1
        return count
    
    def manhattan_dist(self, state):
        count = 0

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    continue
                if state[i][j] != self.goal_state[i][j]:
                    index = np.where(self.goal_state == 0)
                    count += abs(i-index[0][0] + abs(j-index[1][0]))
        return count
    
    def run_hamming(self):

        a = (self.hamming_priority(self.initial_state), 0, self.state_id_counter,self.initial_state)
        open = PriorityQueue()
        closed = set()
        open.put(a)
        self.length+=1
        nodes_taken_out= 0
        parent_map = {}
        while not (open.empty()):
            nodes_taken_out+=1
            curr = open.get()
            closed.add(tuple(map(tuple, curr[3])))
            neighb = self.get_successors(curr[3])
            # print("curr", curr)
            # print("neighbours", neighb)
            if self.is_goal(curr[3]):
                path = []
                while not np.array_equal(curr[3], self.initial_state):
                    path.append(curr[3])
                    curr = parent_map[tuple(map(tuple, curr[3]))]

                path.append(self.initial_state)
                self.state_id_counter
                return path[::-1], len(path), nodes_taken_out
            for i in neighb:
                if tuple(map(tuple, i)) not in closed:
                    neigh_gn = curr[1] + 1
                    neigh_priority = self.hamming_priority(i) + neigh_gn
                    self.state_id_counter+=1
                    open.put((neigh_priority, neigh_gn, self.state_id_counter, i))
                    parent_map[tuple(map(tuple, i))] = curr
            # print()
            # print("Closed_set: ", self.closed)
            # print("Open_set: ", self.open.get())
            
            self.length+=1

    def run_manhattan(self):
        a = (self.manhattan_dist(self.initial_state), 0, self.state_id_counter,self.initial_state)
        open = PriorityQueue()
        closed = set()
        open.put(a)
        self.length+=1
        nodes_taken_out= 0
        parent_map = {}
        while not (open.empty()):
            nodes_taken_out+=1
            curr = open.get()
            closed.add(tuple(map(tuple, curr[3])))
            neighb = self.get_successors(curr[3])
            # print("curr", curr)
            # print("neighbours", neighb)
            if self.is_goal(curr[3]):
                path = []
                while not np.array_equal(curr[3], self.initial_state):
                    path.append(curr[3])
                    curr = parent_map[tuple(map(tuple, curr[3]))]

                path.append(self.initial_state)
                
                self.state_id_counter
                return path[::-1], len(path), nodes_taken_out
            for i in neighb:
                if tuple(map(tuple, i)) not in closed:
                    neigh_gn = curr[1] + 1
                    neigh_priority = self.manhattan_dist(i) + neigh_gn
                    self.state_id_counter+=1
                    open.put((neigh_priority, neigh_gn, self.state_id_counter, i))
                    parent_map[tuple(map(tuple, i))] = curr
            # print()
            # print("Closed_set: ", self.closed)
            # print("Open_set: ", self.open.get())
            
            self.length+=1



    

input = [7, 2, 4, 5, 0, 6, 8, 3, 1]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
input = np.array(input)
input = input.reshape(3,3)
goal = np.array(goal)
goal = goal.reshape(3,3)



x = Puzzle(input, goal)
start = timeit.timeit()
path1, l1, n1 = x.run_manhattan()
end = timeit.timeit()
t1 = end-start
start1 = timeit.timeit()
path2, l2, n2 = x.run_hamming()
end1 = timeit.timeit()
t2 = end1-start1
print("Manhattan Distance: ")
print(f"Time: {t1}, length of soln: {l1}, nodes taken out: {n1}\n")

print("Hamming Priority: \n")
print(f"Time: {t2}, length of soln: {l2}, nodes taken out: {n2}\n")


# for i in y:
#     print(i)
#     print()



    