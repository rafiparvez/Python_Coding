def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    dp = [[0]*len(s) for _ in range(len(s))]
    #since each single character is palindromic with len=1
    for i in range(n):
        dp[i][i] = 1

    #current lenght of substring
    k=2
    while(k <= n):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        k+=1


    print('lenght of longest palin subsequence =', dp[0][n-1], '\nAnd the sub-string is:')
    return getPalin(s, dp, dp[0][n-1])


def getPalin(s, dp, palinLen):
    palin = [None]* palinLen
    i = 0
    j = len(s) - 1

    left = 0
    right = palinLen-1

    while(i<=j):
        if i == j:
            palin[left] = s[i]
            i+=1
        elif s[i] ==  s[j]:
            palin[left] = s[i]
            i+=1
            left+=1
            palin[right] = s[j]
            j-=1
            right-=1
        else:
            if dp[i+1][j] > dp[i][j-1]:
                i+=1
            else:
                j-=1
    return ''.join(palin)



print(longestPalindrome('agbdba'))