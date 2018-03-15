class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        dummy_head = ListNode(-float('inf'))

        # Assuming first node is sorted
        unsorted_head = head

        while (unsorted_head):
            insert_val = unsorted_head.val
            curr_node = dummy_head
            while (curr_node and (insert_val > curr_node.val)):
                prev_node = curr_node
                curr_node = curr_node.next

            prev_node.next = ListNode(insert_val)
            prev_node.next.next = curr_node
            unsorted_head = unsorted_head.next

        return head.next


Node = ListNode(2)
Node.next = ListNode(1)


res = Solution().insertionSortList(Node)