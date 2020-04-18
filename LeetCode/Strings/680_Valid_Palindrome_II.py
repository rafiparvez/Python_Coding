class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin_range(i, j):
            while (i <= j):
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        i = 0
        j = len(s) - 1

        if is_palin_range(i, j):
            return True

        while (i <= j):
            if s[i] != s[j]:
                return is_palin_range(i + 1, j) or is_palin_range(i, j - 1)
            i += 1
            j -= 1
        return True
