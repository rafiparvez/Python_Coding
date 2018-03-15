
num=3
mat = [[i for i in range(num*j - num+1,num*j +1)] for j in range(1,num+1)]
for row in mat:
    print(row)

mat = [[2,3]]

rowMin=0
rowMax=len(mat)-1
colMin=0
colMax=len(mat[0])-1

result =[]
while(rowMin<=rowMax and colMin<=colMax):
    for c in range(colMin,colMax+1):
        result.append(mat[rowMin][c])
        rowMin+=1

    for r in range(rowMin,rowMax+1):
        result.append(mat[r][colMax])
        colMax-=1

    for c in range(colMax,colMin-1,-1):
        result.append(mat[rowMax][c])
