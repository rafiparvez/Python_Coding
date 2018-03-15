class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head

        # 1. Divide the list into halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        l1 = head

        # .2 Sort the lists
        l1_sorted = self.sortList(l1)
        l2_sorted = self.sortList(l2)

        # 3. Merge Sorted Lists
        p = ListNode(0)
        resultNode = p
        while (l1_sorted and l2_sorted):
            if l1_sorted.val < l2_sorted.val:
                p.next = l1_sorted
                l1_sorted = l1_sorted.next
            else:
                p.next = l2_sorted
                l2_sorted = l2_sorted.next
            p = p.next
        if l1_sorted:
            p.next = l1_sorted
        elif l2_sorted:
            p.next = l2_sorted

        return resultNode.next


Node = ListNode(2)
Node.next = ListNode(1)


res = Solution().sortList(Node)