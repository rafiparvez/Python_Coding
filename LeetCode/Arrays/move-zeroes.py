'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = 0
    while (r < len(nums)):
        if nums[r] != 0:
            nums[l] = nums[r]
            l += 1
        r += 1
    while(l<len(nums)):
        nums[l]=0
        l+=1
    return nums

#print(moveZeroes([0,1,0,3,12]))

print(moveZeroes([1,2,0,3,12]))