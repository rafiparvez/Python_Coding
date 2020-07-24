from collections import Counter


def minWindow(s: str, t: str) -> str:

    pat_ctr = Counter(t)
    check_ctr = Counter()

    found_char_set = set()

    l, r = 0, 0

    min_len = float('inf')
    min_str = ''

    while r < len(s):
        char_r = s[r]
        if char_r in pat_ctr:
            check_ctr[char_r] += 1

            if check_ctr[char_r] >= pat_ctr[char_r]:
                found_char_set.add(char_r)

        while len(found_char_set) == len(pat_ctr):
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_str = s[l:r+1]

            char_l = s[l]
            if char_l in pat_ctr:
                check_ctr[char_l] -= 1
                if check_ctr[char_l] < pat_ctr[char_l]:
                    found_char_set.remove(char_l)
            l += 1
        r += 1
    return min_str


s_str = "adfacaabekbaca"
t_str = "aabc"

s_str = "aa"
t_str = "aa"
print(minWindow(s_str, t_str))
