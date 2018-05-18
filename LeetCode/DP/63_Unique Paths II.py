class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[None] * cols for _ in range(rows)]

        dp[0][0] = 1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                elif r == 0:
                    dp[r][c] = dp[r][c - 1] if c > 0 else dp[r][c]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] if r > 0 else dp[r][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


