class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            # non-rotated part in left half
            if nums[start] <= nums[mid]:
                # target in left half
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                # non-rotated part in right half
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid - 1
        return -1
