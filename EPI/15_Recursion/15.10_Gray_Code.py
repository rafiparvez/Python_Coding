'''
Solution: To generate gray codes for n-bits
1. Let list L1 stores gray codes of n-1
2. Generate list L2 which stores reverse of L1
3. Now prefix each code in L1 with 0 and prefix each code in L2 with 1
4. Concatenate L1 and L2

Complexity:
Since L1 has
T(n) = T(n-1) + O(2^n-1)
=> T(n) = O(2^n)
'''

def graycode(n):
    if n==0:
        return [0]

    L1 = graycode(n - 1)
    L2 =list(reversed(L1))

    #L1 doesn't require prefixing with 0 since it implicitly contains prefixed 0
    #L2 can be prefixed with 1 by ORing with a leading_bit_one

    leading_bit_one= 1 << (n-1)

    L2 = [leading_bit_one|code for code in L2]

    return L1+L2

print(graycode(3))

'''
Solution:2
LOGIC:
1.The Most Significant Bit (MSB) of the gray code is always equal to the MSB of the given binary code.
2. Other bits of the output gray code can be obtained by XORing binary code bit at that index and previous index

(right_shift)^(binary code) = (gray code)
(000)^(000) = 000
(000)^(001) = 001
(001)^(010) = 011
(001)^(011) = 010
(010)^(100) = 110
(010)^(101) = 111
(011)^(110) = 101
(011)^(111) = 100

'''
def graycode_2(n):
    ans = [(i >> 1) ^ i for i in range(1<<n)]
    return ans

print(graycode_2(3))