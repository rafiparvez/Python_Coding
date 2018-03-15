# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []

        if not root:
            return result

        # represents all nodes at current level
        level = [root]

        while (level):
            result.append([node.val for node in level])
            child_level = []
            for node in level:
                if node.left: child_level.append(node.left)
                if node.right: child_level.append(node.right)

            level = child_level
        return result
