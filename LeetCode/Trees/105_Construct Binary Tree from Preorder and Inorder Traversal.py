# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return

        root_val = preorder.pop(0)
        idx = inorder.index(root_val)

        root = TreeNode(root_val)
        left_sub_inorder = inorder[0:idx]
        right_sub_inorder = inorder[idx + 1:]

        root.left = self.buildTree(preorder, left_sub_inorder)
        root.right = self.buildTree(preorder, right_sub_inorder)

        return root


