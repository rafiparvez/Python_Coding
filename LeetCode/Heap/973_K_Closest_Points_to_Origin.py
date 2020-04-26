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


# Approach 2: Using Quick Select
"""
Quick select returns Kth smallest element in an array
During quick select, it partitions data in two buckets, the left bucket has 
elements less than the pivot element while right bucket has elements greater 
than the pivot element.
When is quick select returns pivot index at k-th index, it means, all elements
from 0 to k-1 are less than element at k-th index.
"""


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K > len(points):
            return

        def quick_select(points, left, right):
            pivot = left
            left += 1
            while True:
                if left > right:
                    break
                if points[left][0] <= points[pivot][0]:
                    points[left], points[pivot] = points[pivot], points[left]
                    pivot = left
                    left += 1
                elif points[right][0] > points[pivot][0]:
                    right -= 1
                else:
                    points[left], points[right] = points[right], points[left]
            return pivot

        dist_point_arr = []
        for point in points:
            dist_point_arr.append((point[0] ** 2 + point[1] ** 2, point))
        left, right = 0, len(points) - 1

        while True:
            partition_idx = quick_select(dist_point_arr, left, right)
            if partition_idx == K - 1:
                output = [dist_point[1] for dist_point in dist_point_arr[0:K]]
                return output

            elif partition_idx < K - 1:
                left = partition_idx + 1
            else:
                right = partition_idx - 1
