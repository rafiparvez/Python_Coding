#The Power Sum

'''
Solution 1: Brute Force Recursion
Enumerate through all possible combinations
'''

X=800
N=2

def powerSum(target,root, N, num):
    new_target = target-num**N
    if (num >root | new_target<0):
        return 0
    elif new_target==0:
        return 1
    else:
        return powerSum(target,root,N,num+1) + powerSum(new_target,root,N,num+1)

#Nth root of x
root = int(X**(1/N))
print(powerSum(X, root, N ,1))


'''

'''

