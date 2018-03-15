import sys

def thirdMax(nums):
    max_1 = ~sys.maxsize
    max_2 = ~sys.maxsize
    max_3 = ~sys.maxsize

    for n in nums:
        if n > max_1:
            max_1, max_2, max_3 = n, max_1, max_2
        elif n==max_1:
            continue
        elif n > max_2:
            max_2, max_3 = n, max_2
        elif n==max_2:
            continue
        elif n > max_3:
            max_3 = n
    if max_1 == ~sys.maxsize: return None
    elif max_3 == ~sys.maxsize: return max_1
    return max_3

print(thirdMax([2,2,3,1]))