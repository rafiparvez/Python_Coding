def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stk = [-1]
    maxlen = 0

    for i in range(len(s)):
        if s[i] == '(':
            stk.append(i)

        else:
            stk.pop()
            if stk:
                maxlen = max(maxlen, i - stk[-1])
            else:
                stk.append(i)

    return maxlen


print(longestValidParentheses(")"))