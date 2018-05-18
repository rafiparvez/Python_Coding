from collections import Counter
import copy
def get_powerset(nums):
    powerset = []
    hmap = Counter(nums)
    keys = list(hmap.keys())

    def recurse(subset, pos):
        powerset.append(copy.deepcopy(subset))
        for i in range(pos, len(keys)):
            key = keys[i]
            #if current key count gets exhausted, move to next one
            if hmap[key] == 0:
                continue

            hmap[key]-=1
            subset.append(key)
            recurse(subset, i)
            hmap[key] += 1
            subset.pop()


    recurse([], 0)
    return powerset


nums = [1,1,2,3]
print(get_powerset(nums))