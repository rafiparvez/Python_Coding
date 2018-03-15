# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if (not head) or (not head.next):
            return True

        s, f = head, head

        while (f and f.next):
            s = s.next
            f = f.next.next

        # if odd
        if f:
            s = s.next

        # reverse second half LL
        prev = None
        while (s):
            temp = s
            s = s.next
            temp.next = prev
            prev = temp

        while prev:
            if prev.val == head.val:
                prev = prev.next
                head = head.next

            else:
                return False
        return True