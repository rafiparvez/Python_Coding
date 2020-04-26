from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        r = l + len(p) - 1
        p_chars = Counter(p)
        window_chars = Counter()

        output = []

        for char in s[l:r]:
            window_chars[char] += 1

        while (r < len(s)):
            r_char = s[r]
            window_chars[r_char] += 1
            if window_chars == p_chars:
                output.append(l)
            l_char = s[l]
            window_chars[l_char] -= 1
            if window_chars[l_char] == 0:
                del window_chars[l_char]
            l += 1
            r += 1

        return output


