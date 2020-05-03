class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        self.max_palin_len = 1
        self.max_substr = s[0]
        N = len(s)
        dp = [[None] * N for _ in range(N)]
        len_substr = 1
        while len_substr <= len(s):
            for start in range(N - len_substr + 1):
                end = start + len_substr - 1
                if end - start <= 1:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = dp[start + 1][end - 1] and \
                                     s[start] == s[end]

                if dp[start][end]:
                    new_max_palin_len = end - start + 1
                    if new_max_palin_len > self.max_palin_len:
                        self.max_palin_len = new_max_palin_len
                        self.max_substr  = s[start : end +1]

            len_substr += 1

        return self.max_substr
print(Solution().longestPalindrome("aaa"))




