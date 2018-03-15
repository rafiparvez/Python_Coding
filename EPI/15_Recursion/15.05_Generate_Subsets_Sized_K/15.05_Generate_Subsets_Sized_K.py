
result=[]
def get_combination(input_set, k):
    if len(input_set) ==k:
        result.append(input_set)
        return

    elif len(input_set) > k:
        for num in input_set:
            aux_set = input_set.copy()
            aux_set.remove(num)
            get_combination(aux_set, k)
    return result

set = {1,2,3,4}
print(get_combination(set,2))