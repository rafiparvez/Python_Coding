'''
Approach 1:
Step A: Find transpose
Step B: Reverse columns (anti-clockwise)/ Reverse rows(clockwise)
'''

num = 4
a = [[i for i in range(4*j -3,4*j +1)] for j in range(1,num+1)]

def transposeImage(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            a[i][j],a[j][i] = a[j][i], a[i][j]
    return a

def reverseRow(a):
    for i in range(len(a)):
        for j in range(len(a)//2):
            a[i][j],a[i][~j] = a[i][~j],a[i][j]
    return a

def rotateImage(a):
    A_t = transposeImage(a)
    print(A_t)
    return reverseRow(A_t)

print(rotateImage(a))