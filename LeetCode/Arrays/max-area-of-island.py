
#dfs approach
def maxAreaOfIsland(grid):
    max_area = 0
    n_rows = len(grid)
    n_cols = len(grid[0])
    for r in range(n_rows):
        for c in range(n_cols):
            max_area = max(max_area, AreaOfIsland(r,c, grid))
    return max_area

def AreaOfIsland(r, c, grid):
    #if a cell is 1 check for 1 in neightboring cells
    #r and c must lie within valid ranges
    if (r in range(len(grid))) and (c in range(len(grid[0]))) and (grid[r][c]==1):
        #set visited grid to -1
        grid[r][c]=-1
        return 1 + AreaOfIsland(r,c+1, grid) + AreaOfIsland(r,c-1, grid) + \
               AreaOfIsland(r+1,c, grid) + AreaOfIsland(r-1,c, grid)
    else:
        return 0



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]


print(maxAreaOfIsland(grid))