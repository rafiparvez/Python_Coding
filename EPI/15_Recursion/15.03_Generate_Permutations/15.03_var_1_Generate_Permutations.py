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


