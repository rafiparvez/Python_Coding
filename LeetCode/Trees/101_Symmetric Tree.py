# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Approach 1: Recursive
class Solution1(object):
    def isSymmetric(self, root):

        def isMirrored(root1, root2):
            if (not root1) and (not root2):
                return True

            elif (not root1) or (not root2):
                return False

            elif root1.val != root2.val:
                return False

            else:
                return isMirrored(root1.left, root2.right) and isMirrored(root1.right, root2.left)

        return isMirrored(root, root)


# Approach 2: Iterative

class Solutions(object):
    def isSymmetric(self, root):

        stack = [(root, root)]

        while (stack):
            t1, t2 = stack.pop()
            if not t1 and not t2:
                continue

            elif not t1 or not t2:
                return False

            elif t1.val != t2.val:
                return False

            else:
                stack.append((t1.left, t2.right))
                stack.append((t2.left, t1.right))

        return True



