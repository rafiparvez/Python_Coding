'''
Permutations of an array ith duplicate integers
'''

def permutation(num_array):
    res=[]
    if len(num_array) <= 1:
        return [num_array]
    for num in set(num_array):
        temp_array = num_array.copy()
        temp_array.remove(num)
        res += [[num] + perm for perm in permutation(temp_array)]
    return res

arr=[1,2,2]
print(permutation(arr))


#### approach 2

from collections import Counter
from copy import deepcopy

def permute_ii(arr):
    result = []
    hmap = Counter(arr)

    def recurse(arr, idx):
        if idx == len(arr):
            result.append(deepcopy(arr))
            return

        for key in hmap.keys():
            if hmap[key] == 0:
                continue
            hmap[key] -= 1
            arr[idx], key = key, arr[idx]
            recurse(arr, idx+1)
            arr[idx], key = key, arr[idx] # backtrack
            hmap[key] += 1 # backtrack

    recurse(arr, 0)
    return result

arr = [2,3,2]
print(permute_ii(arr))

