class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romanDict = dict()
        romanDict['I'] = 1
        romanDict['V'] = 5
        romanDict['X'] = 10
        romanDict['L'] = 50
        romanDict['C'] = 100
        romanDict['D'] = 500
        romanDict['M'] = 1000

        idx = 0

        res = 0

        while (idx < len(s) - 1):
            if romanDict[s[idx]] < romanDict[s[idx + 1]]:
                res -= romanDict[s[idx]]
            else:
                res += romanDict[s[idx]]
            idx += 1
        res += romanDict[s[idx]]

        return res


