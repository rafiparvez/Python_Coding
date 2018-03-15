import operator


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        operatorDict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        for elt in tokens:
            if elt in ('+', '-', '*', '/'):
                B = stack.pop()
                A = stack.pop()
                output = operatorDict[elt](A, B)
                stack.append(int(output))
            else:
                stack.append(int(elt))

        return stack.pop()
