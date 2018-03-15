'''
Iterative Approach:
Time Complexity: n*[1+2+4+8+...2^(n-1)] = n*2^n
'''

def power_set(input_set):
    powerset=[set()]
    for s in input_set:
        new_sets = [{s}|element for element in powerset]
        powerset+=new_sets
    return powerset

input_set = {1,2,3,3}
print(power_set(input_set))
