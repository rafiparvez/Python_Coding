# ITERATIVE POSTORDER TRAVERSALS

'''
Approach 1: using 2 Stacks
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        stack1 = [root]
        stack2 = []

        while (stack1):
            curr = stack1.pop()
            stack2.append(curr)
            if curr.left:
                stack1.append(curr.left)

            if curr.right:
                stack1.append(curr.right)
        while (stack2):
            result.append(stack2.pop().val)

        return result




'''
Approach 2: using 1 Stack and Flag
'''


class Solution2:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        stack = [(root, False)]

        while (stack):
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)

                else:
                    # post-order traversal

                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result