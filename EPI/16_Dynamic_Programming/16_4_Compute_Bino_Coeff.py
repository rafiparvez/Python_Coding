def binomial_coeff(n,k):
    dp = [[0]*(n+1) for _ in range(k+1)]
    for r in range(k+1):
        for c in range(r,n+1):
            if r==0:
                dp[r][c] = 1
            else:
                dp[r][c] = dp[r][c-1] + dp[r-1][c-1]
    return dp[-1][-1]

print(binomial_coeff(5,3))