"""
1. Depth-First Search (Recursive Approach)

1.a. inorder traversal
1.b. preorder traversal
1.c. postorder traversal
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


""" Constructed binary tree is
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)



# recursive approach
def inorder_rec(tree_root:Node):
    output = []
    def helper_inorder_rec(root):
        if root:
            helper_inorder_rec(root.left)
            output.extend([root.val])
            helper_inorder_rec(root.right)
    helper_inorder_rec(tree_root)
    return output 
    

print("\nRecursive inorder traversal...")
print(inorder_rec(root))

# non-recursive approach
def inorder(root):
    output = []
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            output.append(root.val)
            root = root.right
    return output
print("\nNon-recursive inorder traversal...")
print(inorder(root))
