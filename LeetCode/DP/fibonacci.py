'''
Recursion
'''


def fib1(n):
    if n<=1:
        return n
    return fib1(n-1) + fib1(n-2)

print(fib1(4))


'''
DP: Top-down (Memoization)
'''

def fib2(n, cache={}):
    if n<=1:
        return n
    if n not in cache:
        cache[n] = fib2(n-1) + fib2(n-2)
    return cache[n]
print(fib2(4))


'''
DP: Bottom-Up (Tabulation)
'''

def fib3(n):
    if n <=1:
        return n
    fib_n_1, fib_n_2 = 0,1
    for _ in range(n):
        fib_n = fib_n_1 + fib_n_2
        fib_n_1, fib_n_2 = fib_n, fib_n_1
    return fib_n_1

print(fib3(4))