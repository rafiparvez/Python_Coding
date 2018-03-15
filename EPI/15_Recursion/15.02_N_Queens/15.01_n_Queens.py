'''
find non-attacking placements of n queens in an n x n chessboard.
2 queens cannot exist in same row.
'''

import copy
# function to check if placing queen is safe at board[row][col]
def isSafe(board, row, col):
    # check same column in rows previously checked
    for r in range(row):
        # check for any queen in same column
        if board[r][col] == 1: return False

    # check for down going diagonal
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1: return False

    # check for up going diagonal
    for r, c in zip(range(row, -1, -1), range(col, n, 1)):
        if board[r][c] == 1: return False
    return True

def n_queens(board):
    result = []
    # helper function to process each row
    def n_queens_util(row):
        if row  == n: # all n Queens have already been placed in rows 0,1,.., n-1
            result.append(copy.deepcopy(board))
            return
        for col in range(n):
            if isSafe(board, row, col):
                board[row][col] = 1
                n_queens_util(row + 1)
                board[row][col] = 0

    n_queens_util(0)
    return result


n=4
board = [[0]*n for _ in range(n)]
results= n_queens(board)
print("For #queens =",n,", there are" , len(results), " solutions as follows.")
for i, res in enumerate(results):
    print('\n**Solution:',i+1, '**')
    print('\n'.join('  '.join(str(x) for x in row) for row in res))
