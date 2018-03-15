'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generatePascal(numRows):
    if numRows==0:
        return []
    result=[[1]]
    for i in range(1,numRows):
        prev_row = result[-1]
        new_row = [elt[0]+elt[1] for elt in zip([0]+prev_row, prev_row+[0])]
        result.append(new_row)
    return result


print(generatePascal(3))