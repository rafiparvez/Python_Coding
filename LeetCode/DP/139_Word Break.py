"""
Solution1: Recursive Approach

Complexity Analysis

Time complexity : O(2^n).
https://leetcode.com/problems/word-break/discuss/169383/The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below


Word Break Problem | Dynamic Programming | GeeksforGeeks
https://www.youtube.com/watch?v=hLQYQ4zj0qg

Space complexity : O(n). The depth of the recursion tree can go upto n.

"""


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
            sub_str = s[0: i]
            rest_str = s[i : len(s)]
            if sub_str in wordDict and self.wordBreak(rest_str, wordDict):
                return True

        return False


s = "leetcode"
wordDict = ["leet","code"]


print(Solution1().wordBreak(s,wordDict))



"""
Solution2: Recursion with memoization

Complexity Analysis

Time complexity : O(n^2)
  Size of recursion tree can go up to n^2

Space complexity : O(n). The depth of recursion tree can go up to n.

"""

from typing import List


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        hash_map = dict()

        def helper(string):
            if string == '':
                return True

            if string in hash_map:
                return hash_map[string]

            for i in range(1, len(string) + 1):
                substr = string[0: i]
                rest_str = string[i:]

                if substr in word_set and helper(rest_str):
                    hash_map[string] = True
                    return True
            hash_map[string] = False
            return False

        return helper(s)



s = "abcd"
wordDict = ["a","b", "c", "bc", "abc", "cd"]

print(Solution2().wordBreak(s,wordDict))

"""
Solution 3: Using DP
"""

from collections import defaultdict


class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = defaultdict(int)
        dp[0] = True

        # i points to len of substring from beginning i.e. s[:i]
        for i in range(1, len(s) + 1):
            # j points to partition in substring s[:i] and
            # gives s[:j] and s[j:i]
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    # s[:i] is wordbreak
                    dp[i] = True
                    break

        return dp[len(s)]

s = "abcd"
wordDict = ["a","b", "c", "bc", "abc", "cd"]

print(Solution3().wordBreak(s,wordDict))
