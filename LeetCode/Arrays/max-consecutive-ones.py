'''
Given a binary array, find the maximum number of consecutive 1s in this array.
'''


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_ones = 0
    current_ones = 0
    for n in nums:
        if n == 1:
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0

    return max_ones

nums = [0,1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))