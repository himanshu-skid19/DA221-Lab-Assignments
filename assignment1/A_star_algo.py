import numpy as np
from queue import PriorityQueue
import time

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.length = 0
        self.state_id_counter = 0
        self.dim = self.initial_state.shape[0]
        self.precompute_goal_positions()

    def is_goal(self, state):
        if (state==self.goal_state).all():
            return True
        return False
    
    def test(self):
        print(self.dim)


    def get_successors(self, state):
        index = np.where(state == 0)
        moves = [(index[0][0]+ 1, index[1][0]), (index[0][0]-1, index[1][0]), (index[0][0], index[1][0]+1), (index[0][0], index[1][0] - 1)]
        successors = []
        for i in moves:
            if (0 <= i[0] < state.shape[0]) and ((0 <= i[1] < state.shape[1])):
                state[index[0][0], index[1][0]], state[i[0], i[1]] = state[i[0], i[1]], state[index[0][0], index[1][0]]
                successors.append(state.copy())
                state[index[0][0], index[1][0]], state[i[0], i[1]] = state[i[0], i[1]], state[index[0][0], index[1][0]]
        return successors
    
    def hamming_priority(self, state):
        count = 0
        # print(state)
        
        for i in range(self.dim):
            for j in range(self.dim):
                if state[i][j] == 0:
                    continue
                if state[i][j] != self.goal_state[i][j]:
                    count +=1
        return count
    
    def manhattan_dist(self, state):
        count = 0

        for i in range(self.dim):
            for j in range(self.dim):
                if state[i][j] == 0:
                    continue
                if state[i][j] != self.goal_state[i][j]:
                    index = self.goal_positions[state[i][j]]
                    count += abs(i-index[0]) + abs(j-index[1])
        return count
    

    def precompute_goal_positions(self):
        self.goal_positions = {}
        for i in range(self.dim):
            for j in range(self.dim):
                self.goal_positions[self.goal_state[i][j]] = (i,j)

    def linear_conflict(self, state):
        conflict = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if state[i][j] != 0 and state[i][j] != self.goal_state[i][j]:
                    correct_row, correct_col = self.goal_positions[state[i][j]]
                    if i == correct_row:
                        for k in range(j+1, self.dim):
                            if state[i][k] != 0 and i == self.goal_positions[state[i][k]][0]:
                                if state[i][k] < state[i][j]:
                                    conflict += 2
                    if j == correct_col:
                        for k in range(i+1, self.dim):
                            if state[k][j] != 0 and j == self.goal_positions[state[k][j]][1]:
                                if state[k][j] < state[i][j]:
                                    conflict += 2
        return conflict
    
    def run_hamming(self):
        start = time.time()
        a = (self.hamming_priority(self.initial_state), 0, self.state_id_counter,self.initial_state)
        open = PriorityQueue()
        closed = set()
        open_set_tracker = {tuple(map(tuple, self.initial_state))}
        open.put(a)
        self.length+=1
        nodes_taken_out= 0
        parent_map = {}
        while not (open.empty()):
            # print(f"Iternation{nodes_taken_out}")
            nodes_taken_out+=1
            curr = open.get()
            open_set_tracker.discard(tuple(map(tuple, curr[3])))
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
                
                self.state_id_counter = 0
                end = time.time()
                t = end- start
                return t, path[::-1], len(path), nodes_taken_out
            for i in neighb:
                if tuple(map(tuple, i)) not in closed and tuple(map(tuple, i)) not in open_set_tracker:
                    neigh_gn = curr[1] + 1
                    neigh_priority = self.hamming_priority(i) + neigh_gn
                    self.state_id_counter+=1
                    open.put((neigh_priority, neigh_gn, self.state_id_counter, i))
                    parent_map[tuple(map(tuple, i))] = curr
                    open_set_tracker.add(tuple(map(tuple, i)))
            # print()
            # print("Closed_set: ", self.closed)
            # print("Open_set: ", self.open.get())
            
            self.length+=1
    def run_manhattan(self):
        start = time.time()
        a = (self.manhattan_dist(self.initial_state), 0, self.state_id_counter,self.initial_state)
        open = PriorityQueue()
        closed = set()
        open_set_tracker = {tuple(map(tuple, self.initial_state))}
        open.put(a)
        self.length+=1
        nodes_taken_out= 0
        parent_map = {}
        while not (open.empty()):
            # print(f"Iternation{nodes_taken_out}")
            nodes_taken_out+=1
            curr = open.get()
            open_set_tracker.discard(tuple(map(tuple, curr[3])))
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
                self.state_id_counter = 0
                end = time.time()
                t = end- start
                return t, path[::-1], len(path), nodes_taken_out
            for i in neighb:
                if tuple(map(tuple, i)) not in closed and tuple(map(tuple, i)) not in open_set_tracker:
                    neigh_gn = curr[1] + 1
                    neigh_priority = self.manhattan_dist(i) + neigh_gn
                    self.state_id_counter+=1
                    open.put((neigh_priority, neigh_gn, self.state_id_counter, i))
                    parent_map[tuple(map(tuple, i))] = curr
                    open_set_tracker.add(tuple(map(tuple, i)))
            # print()
            # print("Closed_set: ", self.closed)
            # print("Open_set: ", self.open.get())
            
            self.length+=1
        
    def run_manhattan_linear(self):
        start = time.time()
        a = (self.manhattan_dist(self.initial_state) + self.linear_conflict(self.initial_state), 0, self.state_id_counter,self.initial_state)
        open = PriorityQueue()
        closed = set()
        open_set_tracker = {tuple(map(tuple, self.initial_state))}
        open.put(a)
        self.length+=1
        nodes_taken_out= 0
        parent_map = {}
        while not (open.empty()):
            # print(f"Iternation{nodes_taken_out}")
            nodes_taken_out+=1
            curr = open.get()
            open_set_tracker.discard(tuple(map(tuple, curr[3])))
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
                self.state_id_counter = 0
                end = time.time()
                t = end- start
                return t, path[::-1], len(path), nodes_taken_out
            for i in neighb:
                if tuple(map(tuple, i)) not in closed and tuple(map(tuple, i)) not in open_set_tracker:
                    neigh_gn = curr[1] + 1
                    neigh_priority = self.manhattan_dist(i) + self.linear_conflict(i) + neigh_gn
                    self.state_id_counter+=1
                    open.put((neigh_priority, neigh_gn, self.state_id_counter, i))
                    parent_map[tuple(map(tuple, i))] = curr
                    open_set_tracker.add(tuple(map(tuple, i)))
            # print()
            # print("Closed_set: ", self.closed)
            # print("Open_set: ", self.open.get())
            
            self.length+=1



    
# n = 3
# input = [7, 2, 4, 5, 0, 6, 8, 3, 1]
# # input = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# input = np.array(input)
# input = input.reshape(n,n)
# goal = np.array(goal)
# goal = goal.reshape(n,n)



# x = Puzzle(input, goal)
# # print(x.test())


# t1, path1, l1, n1 = x.run_manhattan()


# t2, path2, l2, n2 = x.run_hamming()

# t3, path3, l3, n3 = x.run_manhattan_linear()
# # t2 = end1-start1
# print("Manhattan Distance: ")
# print(f"Time: {t1}, length of soln: {l1}, nodes taken out: {n1}\n")

# print("Hamming Priority: \n")
# print(f"Time: {t2}, length of soln: {l2}, nodes taken out: {n2}\n")

# print("Manhattan Linear: \n")
# print(f"Time: {t3}, length of soln: {l3}, nodes taken out: {n3}\n")



# for i in y:
#     print(i)
#     print()



    