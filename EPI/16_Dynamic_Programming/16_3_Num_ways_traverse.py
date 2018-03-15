class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == [0]:
                    dp[r][c] = 1
                elif c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        return dp[-1][-1]