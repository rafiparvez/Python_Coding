
'''
Recursive Approach
'''
def lcs(X,Y):
    if len(X) ==0 or len(Y)==0:
        return 0

    if X[-1] == Y[-1]:
        return lcs(X[:-1],Y[:-1]) + 1

    else:
        return max(lcs(X, Y[:-1]), lcs(X[:-1], Y))


'''
DP Approach
'''
def lcs_dp(X,Y):
    m = len(X)
    n = len(Y)
    dp = [[None]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j ==0:
                dp[i][j] = 0

                # ith index in dp table corresponds to (i-1) in the string
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X , Y))
print(lcs_dp(X , Y))