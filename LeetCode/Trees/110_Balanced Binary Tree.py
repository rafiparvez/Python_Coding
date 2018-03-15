import collections

def is_balanced(tree):

    '-1 signifies unbalanced status. Anything other than -1 gives height'
    def dfsHeight(tree):
        if not tree:
            return 0

        leftHeight = dfsHeight(tree.left)
        if leftHeight == -1:
            return -1

        rightHeight = dfsHeight(tree.right)
        if rightHeight == -1:
            return -1

        if abs(rightHeight - leftHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight)+1

    return dfsHeight(tree) != -1


"""
Testing the code for following Binary Tree:

Constructed binary tree is 
            A
          /   \
        B      C 
      /          \ 
    D              E
   /
  F 
"""
class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


A = Node(data='A')
B = Node(data='B')
C = Node(data='C')
D = Node(data='D')
E = Node(data='E')
F = Node(data='F')
A.left = B
A.right = C
B.left = D
C.right = E
D.left = F
print(is_balanced(A))