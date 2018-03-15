'''
Given a binary matrix M, find the longest line of consecutive 1s in the matrix.
The line could be horizontal, vertical, diagonal or anti-diagonal.
'''

def longestLine(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])

    col = [0 for i in range(ncol)]
    diag = [0 for i in range(ncol+nrow)]
    antidiag = [0 for i in range(ncol+nrow)]
    #parameters = [[[None for i in range(2)] for j in range(3)] for k in range(10)]

    max_len=0

    for r in range(nrow):
        row=0
        for c in range(ncol):
            if matrix[r][c]==1:
                row+=1
                col[c]+=1
                diag[r+c]+=1
                antidiag[nrow + c-r]+=1

                max_len = max(row, col[c], diag[r+c], antidiag[nrow+c-1])
            else:
                row=0
                col[c]=0
                diag[c+r]=0
                antidiag[nrow+c-r]=0
    return max_len


mat = [[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1],
[0, 0, 0, 1]
       ]

for row in mat:
    print(row)


print(longestLine(mat))