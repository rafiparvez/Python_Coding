
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> \
    List[List[int]]:
        result = []
        i = j = 0
        while i < len(A) and j < len(B):
            left_intersection = max(A[i][0], B[j][0])
            right_intersection = min(A[i][1], B[j][1])

            # Valid intersection
            if left_intersection <= right_intersection:
                result.append([left_intersection, right_intersection])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return result
