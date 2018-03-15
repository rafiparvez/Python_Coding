from BinaryTreeNode import BinaryTreeNode

r = BinaryTreeNode(4)
r.insertLeft(2)
r.insertRight(5)
r.getLeft().insertLeft(1)
r.getLeft().insertRight(3)
#r.getLeft().getLeft().insertLeft(0)
#r.getLeft().getRight().insertRight(2)


t = BinaryTreeNode(2)
t.insertLeft(1)
t.insertRight(3)

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False

        stack = [s]

        while stack != []:
            curr = stack.pop()
            if curr == t:
                return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False

print(Solution().isSubtree(r, t))





