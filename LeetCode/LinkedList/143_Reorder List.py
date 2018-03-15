# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        '''Approach:
        1. split LL into halves
        2. reverse 2nd half
        3. Merge the 2 halves

        '''

        if not head:
            return

        # find mid point
        slow, fast = head, head

        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        node, pre = slow, None

        while (node):
            pre, node.next, node = node, pre, node.next

        first, second = head, pre

        while (second.next):
            first.next, first = second, first.next
            second.next, second = first, second.next





