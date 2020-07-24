import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # sort
        intervals.sort(key=lambda intvl: (intvl[0], intvl[1]))
        rooms = 1
        min_heap = []

        heapq.heapify(min_heap)
        heapq.heappush(min_heap, intervals[0][1])

        for i in range(1, len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            prev_end = heapq.heappop(min_heap)
            if start < prev_end:
                rooms += 1
                heapq.heappush(min_heap, prev_end)
            heapq.heappush(min_heap, end)
        return rooms
