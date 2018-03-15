import  math
import itertools
def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def isValid(board, row, col, val):
        #row contraint
        if any ( val == num for num in board[row]):
            return False

        #col constraint
        if any ( val == board[j][col] for j in range(len(board))):
            return False

        #grid contraint
        grid_size = int(math.sqrt(len(board)+1))
        I = row//grid_size
        J = col//grid_size

        if any (val == board[a + I*grid_size][ b + J*grid_size]
                for (a,b) in itertools.product(range(grid_size), repeat=2)):
            return False


        return True
    def solve(board, row, col):
        if col == len(board):
            col= 0
            row+=1

            if row == len(board): #entire board is solved
                return True

        #skip non-empty cells
        if board[row][col]!=EMPTY:
            return solve(board, row, col+1)

        for val in range(1, len(board)+1):
            if isValid(board, row, col, str(val)):
                board[row][col] = str(val)
                if solve(board, row, col+1):
                    return True
                else:
                    board[row][col] = EMPTY   #backtrack

        return False
    EMPTY = '.'

    #start solving from board[0[0]
    solve(board, 0, 0)

board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]
solveSudoku(board)

print(board)