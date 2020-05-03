class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

from typing import List

"""
Solution 1: Brute Force Approach
Complexity Analysis
Time complexity :  𝑂(𝑁𝑙𝑜𝑔𝑁)  where  𝑁  is the total number of nodes in  𝑘  linked lists.
Collecting all the values costs  𝑂(𝑁)  time.
A stable sorting algorithm costs  𝑂(𝑁𝑙𝑜𝑔𝑁)  time.
Iterating for creating the linked list costs  𝑂(𝑁)  time.
Space complexity :  𝑂(𝑁) .
Sorting cost  𝑂(𝑁)  space (depends on the algorithm you choose).
Creating a new linked list costs  𝑂(𝑁)  space.
"""
def mergeKLists(lists: List[SinglyLinkedList]) -> SinglyLinkedList:
    result_list = []
    for lst in lists:
        node = lst.head
        while node:
            result_list.append(node.data)
            node = node.next
    if not result_list:
        return
    result_list.sort()
    result_ll = SinglyLinkedList()
    for num in result_list:
        result_ll.append(num)
    return result_ll

def generate_input(ip_lists):
    print(f"input = {ip_lists}")
    lists = []
    for ip_lst in ip_lists:
        ll = SinglyLinkedList()
        for num in ip_lst:
            ll.append(num)
        lists.append(ll)
    return lists

lists = generate_input([[1, 4, 5], [1, 3, 4], [2, 6]])
print(f"output = {mergeKLists(lists)}")


"""
Solution 2 : Using a min-heap.
Complexity Analysis
Time complexity :  𝑂(𝑁𝑙𝑜𝑔𝑘) 

The binary heap(represented by priority queue) has k nodes.
Inserting a new node is  𝑂(𝑙𝑜𝑔𝑘) . This operation is done for all N nodes. So, time complexity is  𝑂(𝑁𝑙𝑜𝑔𝑘) 
Compared to previous case,  𝑘<𝑁 , hence,  𝑙𝑜𝑔𝑘<𝑙𝑜𝑔𝑁 
Space complexity :  𝑂(𝑁) .

Creating a new linked list costs  𝑂(𝑁)  space.
"""
from queue import PriorityQueue
def mergeKLists(lists: List[SinglyLinkedList]) -> SinglyLinkedList:
    pq = PriorityQueue()
    result_list = []
    for idx , linked_lst in enumerate(lists):
        if linked_lst:
            node = linked_lst.head
            pq.put((node.data, idx , node))
    while not pq.empty():
        data, idx, node = pq.get()
        result_list.append(data)
        if node.next:
            pq.put((node.next.data, idx, node.next))
    result_ll = SinglyLinkedList()
    for num in result_list:
        result_ll.append(num)
    return result_ll

lists = generate_input([[1, 4, 5], [1, 3, 4], [2, 6]])
print(f"output = {mergeKLists(lists)}")

"""
Solution 3
Merging 2 lists at a time. This will require k-1 merges for k lists.
"""
