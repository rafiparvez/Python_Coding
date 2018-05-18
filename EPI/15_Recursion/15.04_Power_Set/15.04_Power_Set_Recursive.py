'''
Recursive Approach:
Time Complexity:
'''

def power_set(input_set):
    powerset=[set()]
    if not input_set:
        return [set()]
    for s in input_set:
        sub_input_set = input_set.copy()
        sub_input_set.remove(s)
        powerset = power_set(sub_input_set)
        powerset += [{s}|element for element in powerset]
    return powerset

input_set = {1,2,2}
print(power_set(input_set))