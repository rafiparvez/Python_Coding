'''Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1]

'''

def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [elt[0] + elt[1] for elt in zip([0] + row, row + [0])]

    return row

print(getRow(2))