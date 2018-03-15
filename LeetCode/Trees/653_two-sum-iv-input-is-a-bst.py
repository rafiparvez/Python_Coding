'''
set + bfs
'''


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        myset = set()
        stack = [root]

        while (stack):
            node = stack.pop()
            check_val = k - node.val
            if check_val in myset:
                return True
            myset.add(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


'''
Approach 2: using list and BST
'''


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        mylist = []

        def inorder(root):
            if root:
                inorder(root.left)
                mylist.append(root.val)
                inorder(root.right)

        inorder(root)
        l = 0
        r = len(mylist) - 1

        while (l < r):
            if mylist[l] + mylist[r] == k:
                return True
            elif mylist[l] + mylist[r] < k:
                l += 1
            else:
                r -= 1
        return False