# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        pre_slow, slow, fast = None, head, head

        while (fast and fast.next):
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next

        # cut down the left child
        pre_slow.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root

Node = ListNode(-10)
Node.next = ListNode(-3)
Node.next.next = ListNode(0)
Node.next.next.next = ListNode(5)
Node.next.next.next.next = ListNode(9)

Solution().sortedListToBST(Node)