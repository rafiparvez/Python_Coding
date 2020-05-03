arr = [-2,-3,4,-1,-2, 1,5,-3]


## Brute-Force Appraoch: T(n) = O(n^3); S(n) = O(1)

def max_subarray1(arr):
    n = len(arr)
    max_sum = -float('inf')
    for i in range(n):
        for j in range(i+1, n+1):
            subarray_sum = 0
            for k in range(i,j):
                subarray_sum+=arr[k]
            max_sum = max(max_sum, subarray_sum)
    return max_sum

print(max_subarray1(arr))

## DP: Kadane's Algorithm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_curr_subarray_sum = nums[0]
        max_global_subarray_sum = nums[0]

        for i in range(1, len(nums)):
            max_curr_subarray_sum = max(max_curr_subarray_sum + nums[i], nums[i])
            max_global_subarray_sum = max(max_global_subarray_sum, max_curr_subarray_sum)
        return max_global_subarray_sum
