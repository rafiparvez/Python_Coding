# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []

        if not root:
            return output

        def helper(node, depth):
            if not node:
                return
            if depth == len(output):
                output.append(node.val)
            else:
                output[depth] = max(node.val, output[depth])
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)

        return output

'''
Iterative Approach
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes
