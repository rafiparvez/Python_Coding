class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        max_size = max(len(num1), len(num2))
        num1 = num1.zfill(max_size)
        num2 = num2.zfill(max_size)
        hash_map = dict()
        for i in range(10):
            hash_map[str(i)] = i

        carry = 0
        for i in range(max_size - 1, -1, -1):
            carry += hash_map[num1[i]] + hash_map[num2[i]]
            result.append(str(carry % 10))
            carry = carry // 10
        if carry:
            result.append(str(carry))

        result.reverse()

        return "".join(result)
