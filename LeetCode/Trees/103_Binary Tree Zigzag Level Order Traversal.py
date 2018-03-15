# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []
        if not root:
            return result

        level = [root]
        depth = 0

        while (level):
            level_vals = [node.val for node in level]

            # if depth is odd
            if (depth % 2 == 1):
                level_vals.reverse()

            result.append(level_vals)

            child_level = []

            for node in level:
                if node.left: child_level.append(node.left)
                if node.right: child_level.append(node.right)

            level = child_level
            depth += 1

        return result