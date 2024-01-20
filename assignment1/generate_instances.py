from solvability_check import *
from numpy import random

n = 9

def generate_instances(n, num_examples):
    possibilites = [i for i in range(n)]

    instances = []

    while (len(instances)<num_examples):
        c+=1
        trial = possibilites.copy()
        random.shuffle(trial)
        trial = np.array(trial)
        trial = trial.reshape(3,3)
        if (check_solvability(trial, n)):
            instances.append(trial)
        else:
            continue
        pass

    return instances
