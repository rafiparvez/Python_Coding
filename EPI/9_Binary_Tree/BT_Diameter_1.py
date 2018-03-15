'''
Diameter of a binary tree: 0(n2)
Case 1: If diameter passes through tree root, then dia = height of left subtree + height of right subtree +1
Case 2: If diameter does not pass through root, then dia = max(dia of left subtree, dia of right subtree)
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to return height of a tree
def height(tree):
    if not (tree):
        return 0
    return max(height(tree.left), height(tree.right)) + 1


# function to get diameter of a binary tree
def diameter(tree):
    if not (tree):
        return 0
    left_dia = diameter(tree.left)
    right_dia = diameter(tree.right)
    left_ht = height(tree.left)
    right_ht = height(tree.right)

    return max(left_dia, right_dia, left_ht + right_ht + 1)


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

