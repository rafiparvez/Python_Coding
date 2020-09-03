"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

"""


class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for num in nums[1::]:
            temp_max_so_far = max(num, num * max_so_far, min_so_far * num)
            min_so_far = min(num, num * max_so_far, min_so_far * num)
            max_so_far = temp_max_so_far
            result = max(max_so_far, result)
        return result
