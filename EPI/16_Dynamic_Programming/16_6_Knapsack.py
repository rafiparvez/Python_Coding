def knapSack_Recursive(remaining_wt , wts , val , i):
    if i <0 or remaining_wt<=0:
        return 0

    #Item at (n-1)th index
    if wts[i] > remaining_wt:
        return knapSack_Recursive(remaining_wt, wts, val, i-1)


    else:
        return max(val[i] + knapSack_Recursive(remaining_wt-wts[i], wts, val, i-1),  #item is selected
                   knapSack_Recursive(remaining_wt, wts, val, i - 1))




def knapSack_dp(capacity, wts, val):
    n = len(wts)
    dp = [[0]*(capacity+1) for _ in range(n)]

    for i in range(n):
        for j in range(1, capacity+1):
            if i == 0:
                dp[i][j] = val[i]  if wts[i] <=j else 0
            else:
                if wts[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max( val[i] + dp[i-1][j - wts[i]],
                                    dp[i - 1][j])
    return dp[-1][-1]

val = [60, 50, 70, 30]
wts = [5, 3, 4, 2]
W = 5
n = len(wts)
print(knapSack_Recursive(W , wts , val , n-1))

print(knapSack_dp(W, wts, val))