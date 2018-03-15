'''
Space = O(1)
Time = O(n)
Explanation:
I use the variables beg and end to keep track of minimum subarray A[beg_idx...end_idx]
1. If end < beg < 0 at the end of the for loop, then the array is already fully sorted.
2.
end_idx = The rightmost  element having greater elements on the left side.
beg_idx = The leftmost element having smaller elements on the right side.

'''

def findUnsortedSubarray(A):
    class Solution:
        def findUnsortedSubarray(self, nums):
            beg_idx = -1
            end_idx = -2
            n = len(nums)
            max_num = nums[0]
            min_num = nums[n - 1]
            for l_idx in range(1, n):
                r_idx = n - 1 - l_idx
                max_num = max(max_num, nums[l_idx])
                if nums[l_idx] < max_num:
                    end_idx = l_idx

                min_num = min(min_num, nums[r_idx])
                if nums[r_idx] > min_num:
                    beg_idx = r_idx
            return end_idx - beg_idx + 1


l=[2]
print(findUnsortedSubarray(l))