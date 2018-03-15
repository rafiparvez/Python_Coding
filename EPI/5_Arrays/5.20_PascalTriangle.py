"""
Space Complexity = 1+2+...n = O(n^2)
Time Complexity = o(n^2)
"""


def generate_pascal(n):
    result = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1,i):

            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result


print(generate_pascal(5))