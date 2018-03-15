# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dia = 0

        def height_n_dia(root):
            if not root:
                return 0
            left_ht = height_n_dia(root.left)
            right_ht = height_n_dia(root.right)

            self.dia = max(self.dia, left_ht + right_ht)
            return max(left_ht, right_ht) + 1

        height_n_dia(root)
        return self.dia
