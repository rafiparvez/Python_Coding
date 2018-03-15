'''
Diameter of a binary tree: 0(n)
OPTIMIZATION: Can be done by calculating height within same recursive call to calculate diameter.
The function evaluates diameter at each node. The DIAMETER OF ENTIRE TREE OCCURS AT THE NODE FOR WHICH
(LEFT_SUBTREE_HEIGHT+RIGHT_SUBTREE_HEIGHT+1) IS MAXIMUM.

'''

import collections

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to get diameter of a binary tree
def diameter(tree):
    dia = 0
    def height_and_dia(tree):
        nonlocal dia
        if not (tree):
            return 0 #diameter is 0
        lh = height_and_dia(tree.left)
        rh = height_and_dia(tree.right)
        dia = max(dia, lh+rh+1)
        return max(lh, rh)+1

    height_and_dia(tree)
    return dia

"""
Testing the code for following Binary Tree:

Constructed binary tree is 
            1
          /   \
        2      3
      /  \
    4     5
   /       \
  6         7 

"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.right = Node(7)

calls = 0
print("Diameter of given binary tree is %d" % (diameter(root)))

'''
Time Complexity:
For each node there are 2 calls to diameter function, each for it's left and right subtrees.
For n nodes no. of recursive calls = 2n
Within each recursive calls height is calculated for both left and right subtree, which in O(n) operation.
Hence, T(n) = 2n*O(n) = O(n2)
'''

