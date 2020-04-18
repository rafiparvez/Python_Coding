"""
Problem:

Given an list of integers. Find k-th smallest element

"""
from typing import List


def partition(arr, pivot_index, left, right):
    """
    function to return partion index, which is the index where pivot should be
    be places in a sorted array
    :param arr:
    :param pivot_index:
    :return:
    """

    while True:
        if left > right:
            break
        if arr[left] < arr[pivot_index]:
            arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
            pivot_index = left
            left += 1
        elif arr[right] > arr[pivot_index]:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
    return pivot_index


def quick_select(nums: List, k: int)->int:
    if (not nums) or (k > len(nums)):
        return
    pivot_index = 0
    left, right = 1, len(nums) - 1

    while True:
        pivot_index = partition(nums, pivot_index, left, right)
        # k-th smallest element founds, +1 as 1st smallest element occurs at 0
        if pivot_index == k - 1:
            return nums[pivot_index]

        # k-th largest elements occurs in right partition
        elif pivot_index < k - 1:
            pivot_index = pivot_index + 1
            left = pivot_index + 1

        else:
            right = pivot_index - 1
            pivot_index = left - 1

    return None


input_list = [7, 10, 4, 3, 20, 15]  # sorted = [3, 4, 7, 10, 15, 20]

print(quick_select(input_list, 6))
