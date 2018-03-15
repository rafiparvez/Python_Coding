def subsetsWithDup_iterative(S):
    res = [[]]
    S.sort()
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            l = len(res)
        for j in range(len(res) - l, len(res)):
            res.append(res[j] + [S[i]])
    return res


def subsetsWithDup_recursive(nums):
    res = []
    nums.sort()
    helper(nums, 0, [], res)
    return res
def helper(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        helper(nums, i + 1, path + [nums[i]], res)
a = [2,1,2]

print(subsetsWithDup_iterative(a))
print(subsetsWithDup_recursive(a))