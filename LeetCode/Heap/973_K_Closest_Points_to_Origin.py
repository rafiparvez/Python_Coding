# Approach 1: PriorityQueue
"""
Time Complexity:
  - O(N) for heap creation
  - O(Klog(N)) to extract from the heap

Space Complexity:
  - O(N) for heap
  - O(K) for result
"""

from typing import List
from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            pq.put((dist, point))
        result = []
        for i in range(K):
            result.append(pq.get()[1])
        return result


import sys
print(sys.maxsize)
