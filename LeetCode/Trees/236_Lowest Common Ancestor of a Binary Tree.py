# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
O(N)

Explanation:
https://www.youtube.com/watch?v=13m9ZCB8gjw

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        if not root:
            return

        if root == p or root == q:
            return root

        left_node = self.lowestCommonAncestor(root.left, p, q)

        right_node = self.lowestCommonAncestor(root.right, p, q)

        # case1: no ancestor found
        if (not left_node) and (not right_node):
            return

        # case 2: nodes on either side
        elif left_node and right_node:
            return root

        # case 3: one of the nodes found
        elif left_node:
            return left_node
        else:
            return right_node

