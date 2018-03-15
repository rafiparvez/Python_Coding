'''
Solution1: Recusrive Approach
'''

class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if not s:
            return True

        for i in range(1, len(s)+1):
            if (s[0:i] in wordDict) and self.wordBreak(s[i:] , wordDict):
                return True

        return False


s = "leetcode"
wordDict = ["leet","code"]

print(Solution1().wordBreak(s,wordDict))



'''
Solution2: Dynamic Programming Approach
'''


class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if not s:
            return True

        memo = [[-1 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]


        for i in range(1, len(s)+1):
            for j in range(len(s)):
                if s[j:j+i] in wordDict:
                    memo[j][j+i] = j
                    continue

                for k 




s = "leetcode"
wordDict = ["leet","code"]

print(Solution2().wordBreak(s,wordDict))