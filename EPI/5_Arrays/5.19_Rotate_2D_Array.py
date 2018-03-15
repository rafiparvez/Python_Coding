'''
Brute-Force
Space and Time = O(n^2)
'''

def rotate_matrix_1(mat):
    n_rows = len(mat)
    n_cols = len(mat[0])

    #in resuls n_cols becomes n_rows and vice versa
    result_mat=[[0 for x in range(n_rows)] for y in range(n_cols)]

    for c in range(n_cols):
        for r in range(n_rows):
            result_mat[c][n_rows-r-1] = mat[r][c]

    return result_mat


def rotate_matrix_2(mat):
    N = len(mat)

    for r in range(N//2):
        for c in range(r,N-1-r):
            mat[r][c], mat[~c][r], mat[~r][~c], mat[c][~r] = \
                mat[~c][r], mat[~r][~c], mat[c][~r], mat[r][c]
    return mat

'''
3rd approach:
Step A: Find transpose
Step B: Reverse columns (anti-clockwise)/ Reverse rows(clockwise)
'''

def transposeImage(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            a[i][j],a[j][i] = a[j][i], a[i][j]
    return a

def reverseRow(a):
    for i in range(len(a)):
        for j in range(len(a)//2):
            a[i][j],a[i][~j] = a[i][~j],a[i][j]
    return a

def rotate_matrix_3(a):
    A_t = transposeImage(a)
    return reverseRow(A_t)



num = 4
mat = [[i for i in range(4*j -3,4*j +1)] for j in range(1,num+1)]
print(mat)

print(rotate_matrix_1(mat))
print(rotate_matrix_2(mat))

mat = [[i for i in range(4*j -3,4*j +1)] for j in range(1,num+1)]
print(rotate_matrix_3(mat))


