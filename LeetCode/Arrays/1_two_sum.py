class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultdict = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in resultdict:
                return [resultdict[diff], idx]
            else:
                resultdict[num] = idx
        return None