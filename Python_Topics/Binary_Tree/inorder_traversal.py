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


# non-recursive approach
def inorder(root):
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val)
            root = root.right
inorder(root)
