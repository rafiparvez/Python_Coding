# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder:
            return

        # last element is root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        idx = inorder.index(root_val)

        left_sub_inorder = inorder[0:idx]
        right_sub_inorder = inorder[idx + 1:]

        root.right = self.buildTree(right_sub_inorder, postorder)
        root.left = self.buildTree(left_sub_inorder, postorder)

        return root