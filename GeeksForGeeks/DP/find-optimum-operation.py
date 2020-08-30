"""
You are given a number N. You have to find the min number of operations required
to reach N from 0. You have 2 operations available:

Double the number
Add one to the number

"""
import timeit


# Recursion
def min_operations_rec(N):
    if N <= 1:
        return N
    if N % 2 == 0:
        return min(min_operations_rec(N//2), min_operations_rec(N-1)) + 1
    else:
        return min_operations_rec(N-1) + 1


print("recurive approach")
N = 0
print(min_operations_rec(N))
N = 2
print(min_operations_rec(N))
N = 7
print(min_operations_rec(N))
N = 8
print(min_operations_rec(N))


# dp
def min_operations_dp(N):
    min_ops_dict = {0: 0, 1: 1}

    def helper(N):
        if N in min_ops_dict:
            return min_ops_dict[N]
        elif N % 2 == 0:
            res = min(min_operations_dp(N//2),min_operations_dp(N-1)) + 1
        else:
            res = min_ops_dict[N] = min_operations_dp(N - 1) + 1
        min_ops_dict[N] = res
        return res
    helper(N)
    return min_ops_dict[N]


print("\nDP approach")
N = 0
print(min_operations_dp(N))
N = 2
print(min_operations_dp(N))
N = 7
print(min_operations_dp(N))
N = 8
print(min_operations_dp(N))


# compute dp time

# compute binary search time
def get_run_times():
    SETUP_CODE = '''
from __main__ import min_operations_dp, min_operations_rec
from random import randint
    '''

    TEST_CODE_DP = ''' 
num = randint(0, 100)
min_operations_dp(num)
    '''

    TEST_CODE_REC = ''' 
num = randint(0, 100)
min_operations_rec(num)
        '''

    # timeit.repeat statement
    times_dp = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_DP,
                          repeat=2,
                          number=100)

    # timeit.repeat statement
    times_rec = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_REC,
                          repeat=2,
                          number=100)

    # printing minimum exec. time
    print('DP  time: {}'.format(min(times_dp)))
    print('REC  time: {}'.format(min(times_rec)))


if __name__ == '__main__':
    get_run_times()
