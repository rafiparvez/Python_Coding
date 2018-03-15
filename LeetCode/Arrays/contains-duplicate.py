'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
 and it should return false if every element is distinct
'''
def containsDuplicate1(nums):
    if not nums:
        return False
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]: return True
    return False


def containsDuplicate2(nums):
    myset = set()
    for num in nums:
        if num in myset: return True
        else: myset.add(num)
    return False

nums = [1,2,3,1]

print(containsDuplicate1(nums))