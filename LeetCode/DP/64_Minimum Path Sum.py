class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        nrows = len(grid)
        ncols = len(grid[0])

        dp = [[0] * ncols for _ in range(nrows)]

        dp[0][0] = grid[0][0]

        for r in range(nrows):
            for c in range(ncols):
                if r == 0:
                    dp[r][c] = grid[r][c] + dp[r][c - 1] if c > 0 else dp[r][c]

                elif c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c] if r > 0 else dp[r][c]

                else:
                    dp[r][c] = min(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]

        return dp[-1][-1]