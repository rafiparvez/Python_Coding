class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while (x or y):
            res += (x & 1) ^ (y & 1)
            x = x >> 1
            y = y >> 1
        return res