'''
Given an array consisting of n integers, find the contiguous subarray
 of given length k that has the maximum average value. And you need to output the maximum average value.
'''


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    # max sum of first k integers in array
    idx = 0
    current_tot_sum = sum(nums[idx:idx + k])
    max_tot_sum = current_tot_sum

    while (idx + k < len(nums)):
        current_tot_sum = current_tot_sum - nums[idx] + nums[idx + k]
        max_tot_sum = max(max_tot_sum, current_tot_sum)
        idx += 1
    return max_tot_sum / k

nums = [0,4,0,3,2]
k = 3

print(findMaxAverage(nums, k))