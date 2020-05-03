# Approach 1: Using heap tree

from queue import PriorityQueue
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = PriorityQueue()
        # build heap with k elements

        for i in range(k):
            minheap.put((nums[i]))

        for j in range(k, len(nums)):
            # kth-largest element occurs at top of bin heap tree
            kth_element = minheap.queue[0]
            next_num = nums[j]
            if next_num > kth_element:
                # remove top element
                minheap.get()
                minheap.put(next_num)
        return minheap.get()


print(Solution().findKthLargest([3,1,4,5], 2))

# Approach 2: Using quick select

