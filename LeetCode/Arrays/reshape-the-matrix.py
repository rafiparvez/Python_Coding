'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the
wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

'''
nums = [[1,2],
        [3,4],
        [5,6]]
r = 6
c = 1
def matrixReshape1(nums, r, c):
    n_row = len(nums)
    n_col = len(nums[0])

    if not all([r,c,n_row, n_col]) and r*c != n_row*n_col:
        return nums

    output = [[0 for _ in range(c)] for _ in range(r)]

    row = 0
    col = 0
    for i in range(r):
        for j in range(c):
            output[i][j] = nums[row][col]
            col+=1
            if col == n_col:
                row+=1
                col=0
    return output

print(matrixReshape1(nums, r, c))
'''
def matrixReshape2(nums, r, c):
    for i in range(nums):
        for j in range(nums[0]):

    queue = []
'''