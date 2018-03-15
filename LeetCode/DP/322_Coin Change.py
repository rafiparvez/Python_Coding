class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        n = len(coins)

        dp = [[0] + [float('inf')] * (amount) for _ in range(n)]

        for j in range(amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]

        for i in range(1, n):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(1 + dp[i][j - coins[i]],
                                   dp[i - 1][j])

        if dp[-1][-1] == float('inf'):
            return -1
        else:
            return dp[-1][-1]