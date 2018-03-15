'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''
def searchInsert(nums, target):
    l = 0
    r = len(nums)-1

    while(l<r):
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l
print(searchInsert([1,2,3,5,6,7], 4))