'''
Permutations of an array of distinct integers
'''

def permutation(num_array):
    res=[]
    if len(num_array) <= 1:
        return [num_array]
    for num in num_array:
        temp_array = num_array.copy()
        temp_array.remove(num)
        res += [[num] + perm for perm in permutation(temp_array)]
    return res

arr=[1,2,3]
print(permutation(arr))


result=[]

def get_num(arr):
    num = 0
    for n in arr:
        num=10*num + n
    return num

def permute(A, l, r):
    if l==r:
        result.append(get_num(A.copy()))
    for i in range(l,r):
        #to compute all permutations that begin with A[i],
        #Swap A[0] with A[i] and permute A[1, n-1]
        A[l], A[i] = A[i], A[l]
        permute(A, l+1, r)
        A[l], A[i] = A[i], A[l] #backtrack
    return result


A=[1,1,3]
print(permute(A,0,len(A)))


