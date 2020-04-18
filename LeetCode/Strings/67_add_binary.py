
# Approach 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_output = int(a, 2) + int(b, 2)
        bin_output = bin(dec_output)
        return bin_output.replace("0b", "")


# Approach 2

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0
        ans = []

        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            ans.append(str(carry % 2))
            carry = carry // 2

        if carry:
            ans.append(str(carry))
        ans.reverse()

        return ''.join(ans)

