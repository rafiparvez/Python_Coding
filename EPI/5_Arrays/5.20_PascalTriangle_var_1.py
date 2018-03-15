"""
Var 1:
Space Complexity = O(n)
"""
def generate_pascal_nth_row(n):
    result=[1]*n
    for i in range(n):
        previous_res = result.copy()
        for j in range(1,i):
            result[j] = previous_res[j-1] + previous_res[j]
    return result

print(generate_pascal_nth_row(6))


def generate_pascal_nth_row_2(n):
    row = [1]
    for r in range(n-1):
        # Next row of [1,2,1] can be calculates as
        # element by element sum of [0,1,2,1] and [1,2,1,0]
        row = [l + r for l, r in zip(row + [0], [0] + row)]
    # print row
    return row

print(generate_pascal_nth_row_2(6))


'''
Uses
C(n,k+1) = C(n,k) * (n-k) / (k+1)
[1,3,3,1] = [C(3,0),C(3,1),C(3,2),C,(3,3)] 
'''
def generate_pascal_nth_row_3(n):
    n=n-1
    result = [1]
    for k in range(n):
        result.append(int(result[k]*(n-k)/(k+1)))
    return result


print(generate_pascal_nth_row_3(6))