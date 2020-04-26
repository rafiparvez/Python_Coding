class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        balance = 0
        indices_to_remove = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    indices_to_remove.add(i)
                else:
                    stack.pop()
        while stack:
            indices_to_remove.add(stack.pop())

        output_list = []

        for i, char in enumerate(s):
            if i not in indices_to_remove:
                output_list.append(char)

        return ''.join(output_list)

