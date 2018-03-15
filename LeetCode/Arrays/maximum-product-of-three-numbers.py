'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.
'''

'''
Approach 1:
1. Sort the array.
2. if it contains negative elements then max product may also contain 2 leftmost negative numbers

Time Complexity: O(nlog(n)) 
'''

def maximumProduct1(nums):
    nums.sort()
    return max(nums[0]*nums[1]*nums[-1], nums[-3] * nums[-2]* nums[-1])


nums =  [-3,-4,1,2,5]
print(maximumProduct1(nums))


###########################

'''
Approach 2:
In Single Pass, find these elements
1. 2 least elements min_1, min_2
2. 3 largest elements max_1, max_2, max_3

result = max(min_1*min_2*max_3, max_1*max_2*max_3)
Time Complexity: O(n) 
'''
import sys
def maximumProduct2(nums):
    min_1 = sys.maxsize
    min_2 = sys.maxsize

    max_1 = ~sys.maxsize
    max_2 = ~sys.maxsize
    max_3 = ~sys.maxsize
    for num in nums:
        if num < min_1:
            min_1, min_2 = num, min_1
        elif num < min_2:
            min_2 = num

        if num > max_1:
            max_1, max_2, max_3 = num, max_1, max_2
        elif num > max_2:
            max_2, max_3 = num, max_2
        elif num > max_3:
            max_3 = num
    return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)

nums = [9,1,5,6,7,2]
print(maximumProduct2(nums))