import random
import numpy as np


def merge_sort(arr):
    global inversions
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)

        merge_sort(right)

        i = j = k = 0

        while ( i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
            else:
                inversions += len(left) - i
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

def check_solvability(input, n):
    global inversions
    index = np.where(input == 0)[0][0]
    r = input.shape[0]
    index = r - index
    lin = input.reshape(1, n*n)
    lin = lin.tolist()[0]
    lin.remove(0)

    inversions = 0 
    merge_sort(lin)
    if n % 2 == 1:
        if inversions % 2 == 0:
            return True
        else:
            return False
    else:
        if inversions % 2 == 0:
            if index % 2 == 1:
                return True
            else:
                return False
        else: 
            if index % 2 == 0:
                return True
            else:
                return False




n = 4
input = [13, 2, 10, 3, 1, 12, 8, 4, 5, 0, 9, 6, 15, 14, 11, 7]
input = np.array(input)
input = input.reshape(n,n)
# n = input.shape[0]*input.shape[1]
# print(n)

print(check_solvability(input, n))

