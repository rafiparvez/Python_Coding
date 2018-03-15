'''
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one)
and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
'''

def maxDistance(array):
    min_val = array[0][0]
    max_val = array[0][-1]
    result = 0
    for i in range(1, len(array)):
        result = max(result, max(abs(array[i][-1]) - min_val, abs(max_val - array[i][0])))
        min_val = min(min_val, array[0][0])
        max_val = max(max_val, array[0][-1])
    return result
array = [[1,2,3,4,5,6],
 [4,5],
 [2,3,4]]

print(maxDistance(array))