"""
https://www.youtube.com/watch?v=xun6zHlX8kI
"""
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        #dp[i] denotes all word-breaks till a index i
        dp_hashmap = defaultdict(list)
        dp_hashmap[0] = [""]
        for end in range(1, len(s) + 1):
            for start in range(end):
                if start in dp_hashmap:
                    substr = s[start: end]
                    if substr in word_set:
                        for w in dp_hashmap[start]:
                            dp_hashmap[end].append(
                                "{} {}".format(w, substr).strip())
        return dp_hashmap[end]
