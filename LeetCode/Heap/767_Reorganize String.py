from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        max_heap = []
        output = ""
        s_cntr = Counter(S)
        N = len(S)
        for char in s_cntr:
            count = s_cntr[char]
            if count > (N + 1) / 2:
                return ""
            heapq.heappush(max_heap, (-count, char))

        while len(max_heap) >= 2:
            print(max_heap)
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            output += char1 + char2

            if count1 + 1 != 0:
                heapq.heappush(max_heap, (count1 + 1, char1))

            if count2 + 1 != 0:
                heapq.heappush(max_heap, (count2 + 1, char2))

        if len(max_heap) > 0:
            output += heapq.heappop(max_heap)[1]

        return output
