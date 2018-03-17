
def permute(arr):
    result = []

    #l corresponds to the index which is swapped each of it elements to the right
    def helper(arr, l):
        if l == len(arr) - 1:
            result.append(arr.copy())
        for j in range(l, len(arr)):
            arr[l], arr[j] = arr[j], arr[l]
            #now permute rest of the elements
            helper(arr, l+1)
            arr[l], arr[j] = arr[j], arr[l] #backtrack
    helper(arr, 0)
    return result

print(permute([1,2,3]))