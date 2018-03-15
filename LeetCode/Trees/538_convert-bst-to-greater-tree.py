
def convertBST(tree):
    def helper(tree, total):
        if not tree:
            return
        else:
            helper(tree.right, total)
            total += tree.val
            tree.val = total
            helper(tree.left, total)
        return tree
    return helper(tree, 0)


"""
Testing the code for following Binary Tree:

Constructed binary tree is 
        2
      /   \
     1     3
         /
        2.5
"""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(2.5)


tree = convertBST(root)

print(tree.val)