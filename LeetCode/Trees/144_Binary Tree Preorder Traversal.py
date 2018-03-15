class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        stack = [root]
        while (stack):
            node = stack.pop()
            result.append(node.val)
            if (node.right): stack.append(node.right)
            if (node.left): stack.append(node.left)

        return result