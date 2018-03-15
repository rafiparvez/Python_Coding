str1,str2 = 'sunday' , 'saturday'

## Convert str1 --> str2
#Approach 1: Recursive : O(3^n)
def levenshtein_dist(str1,str2):
    def helper(str1, str2, a, b):
        #a, b correspond to last character of the 2 strings

        #if str1 is emply insert all strings of str2
        if a==0:
            return b

        # if str2 is emply insert all strings of str1
        if b==0:
            return a

        if str1[a-1] == str2[b-1]:
            return helper(str1, str2, a-1, b-1)
        else:
            return 1 + min(
                helper(str1, str2, a, b-1),  #insert 1 character in the end of str1
                helper(str1, str2, a-1, b),   #delete 1 character from the end of str1
                helper(str1, str2, a-1, b-1)  #replace last character of str1
            )
    return helper(str1, str2, len(str1), len(str2))

print(levenshtein_dist(str1,str2))


#Approach 2: DP : O()
def levenshtein_dist_dp(str1,str2):
    a = len(str1)
    b = len(str2)

    dp = [[0 for _ in range(b+1)] for _ in range(a+1)]

    for i in range(a+1):
        for j in range(b+1):
            # if first string's length is 0
            # num of edits insert all chars of str1
            if i==0:
                dp[i][j] = j

            # if 2nd string's length is 0
            # num of edits deleting all chars of str2
            elif j == 0:
                dp[i][j] = i

            #if last to characters are same
            #then ignore last 2 chars and recur for remaining
            #strings
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1+min(
                    dp[i][j-1],   #insert
                    dp[i-1][j],   #remove
                    dp[i-1][j-1]  #replace
                )

    return dp[a][b]


print(levenshtein_dist_dp(str1,str2))