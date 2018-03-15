class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = {}

        for i, num in enumerate(nums):
            if num in my_dict and i - my_dict[num] <= k:
                return True
            my_dict[num] = i

        return False