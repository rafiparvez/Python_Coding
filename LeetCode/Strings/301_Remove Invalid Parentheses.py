from typing import List


class Solution:
    def __init__(self):
        self.valid_expressions = set()
        self.min_rem = float('inf')
        self.paren_chars = {'(', ')'}

    def helper(self, s, idx, left_count, right_count, num_rem, expr_arr):
        # current index has reached end of string
        if idx == len(s):
            # balanced expression
            if left_count == right_count:
                if num_rem <= self.min_rem:
                    expr_str = "".join(expr_arr)

                    # got new min, reset the set
                    if num_rem < self.min_rem:
                        self.min_rem = num_rem
                        self.valid_expressions = set()

                    self.valid_expressions.add(expr_str)
        # not reached the end of string
        else:
            curr_char = s[idx]
            if curr_char not in self.paren_chars:
                expr_arr.append(curr_char)
                self.helper(s, idx + 1,
                       left_count, right_count,
                       num_rem, expr_arr)
                expr_arr.pop()
            else:
                # recurse ignoring one char
                self.helper(s, idx + 1,
                            left_count, right_count,
                            num_rem + 1, expr_arr)

                expr_arr.append(curr_char)

                if curr_char == '(':
                    # increment left and move forward
                    self.helper(s, idx + 1,
                                left_count + 1, right_count,
                                num_rem, expr_arr)

                else:
                    if right_count < left_count:
                        # increment right and move forward
                        self.helper(s, idx + 1,
                                    left_count, right_count + 1,
                                    num_rem, expr_arr)
                expr_arr.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.helper(s, 0, 0, 0, 0, [])
        return self.valid_expressions


s = "()())()"
print(Solution().removeInvalidParentheses(s))
