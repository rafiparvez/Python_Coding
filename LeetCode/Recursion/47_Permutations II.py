from collections import Counter
from copy import deepcopy


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        hmap = Counter(nums)

        def recurse(nums, idx):
            if idx == len(nums):
                result.append(deepcopy(nums))

            for key in hmap.keys():
                if hmap[key] == 0:
                    continue
                hmap[key] -= 1
                nums[idx], key = key, nums[idx]
                recurse(nums, idx + 1)

                nums[idx], key = key, nums[idx]
                hmap[key] += 1

        recurse(nums, 0)

        return result

