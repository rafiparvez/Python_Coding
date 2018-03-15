'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    idx = m + n-1
    while (idx >= 0 and m > 0 and n > 0):
        nums1[idx] = max(nums1[m-1], nums2[n-1])
        if nums1[m-1] > nums2[n-1]:
            m -= 1
        else:
            n -= 1
        idx-=1
    if n > 0:
        nums1[:n] = nums2[:n]
    return nums1

nums1=[3,6,7,0,0,0,0]
m=3
nums2=[1,2,4,5]
n=4
print(merge(nums1, m, nums2, n))