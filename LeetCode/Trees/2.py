from BinaryTreeNode import BinaryTreeNode

r = BinaryTreeNode(2)
r.insertLeft(1)
r.insertRight(3)
#r.getLeft().getLeft().insertLeft(0)
#r.getLeft().getRight().insertRight(2)


t = BinaryTreeNode(2)
t.insertLeft(1)
t.insertRight(3)

class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q

print(Solution().isSameTree(r, t))