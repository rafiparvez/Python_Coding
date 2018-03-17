
def permute(arr):
    result = []
    check_set ={}

    #l corresponds to the index which is swapped each of it elements to the right
    def helper(arr, index, n):
        if index >= n:
            result.append(arr.copy())
            return
        for j in range(n):
            if arr[index]!= arr[j]:
                arr[index], arr[j] = arr[j], arr[index]
                helper(arr, index + 1, n)
                arr[index], arr[j] = arr[j], arr[index]  #backtrack

    helper(arr, 0, len(arr))
    return result

print(permute([1,2,2]))