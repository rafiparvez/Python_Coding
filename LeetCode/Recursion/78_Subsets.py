# Iterative Approach

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = [[]]

        for num in nums:
            powerset = powerset + [subset + [num] for subset in powerset]

        return powerset