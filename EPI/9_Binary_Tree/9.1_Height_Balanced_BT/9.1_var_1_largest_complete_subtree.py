import collections

def is_balanced(tree):
    isbalancedWithHeight = collections.namedtuple(
        'isbalancedWithHeight',('isBalanced', 'height'))


    def check_balanced(tree):
        if not tree.left and not tree.right:
            return isbalancedWithHeight(True, 0)

        leftStatus = check_balanced(tree.left)

        if not leftStatus.isBalanced:
            return isbalancedWithHeight(False, 0)

        rightStatus = check_balanced(tree.right)

        if not rightStatus.isBalanced:
            return isbalancedWithHeight(False, 0)

        isBalanced = abs(leftStatus.height - rightStatus.height)<=1
        height = max(leftStatus.height, rightStatus.height)+1
        rootstatus = isbalancedWithHeight(isBalanced, height)
        return (rootstatus)

    result = check_balanced(tree)
    return result.isBalanced

"""
Testing the code for following Binary Tree:

Constructed binary tree is 
            A
          /  \
        B      C  
      /  \
    D     E

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
A.left = B
A.right = C
B.left = D
B.right = E

print(is_balanced(A))