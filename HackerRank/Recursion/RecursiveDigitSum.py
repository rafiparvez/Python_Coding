import sys


def sumdigit(n):
    s = 0
    while (n > 0):
        s += n % 10
        n = n // 10
    return s


def superDigit(n, k):
    # Complete this function
    if (n < 10) & (k == 1):
        return n
    else:
        s = sumdigit(n)
        return superDigit(k*s, 1)


if __name__ == "__main__":
    n, k = [148, 3]
    print(n, k)
    result = superDigit(n, k)
    print(result)