# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Approach 1: Complete Inorder traversal. Create a sorted array from BST
Time Complexity: O(n), n = total nodes
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        inorder_arr = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder_arr.append(root.val)
            inorder(root.right)

        inorder(root)

        print(inorder_arr)

        i = 0
        if target < inorder_arr[0]:
            return inorder_arr[0]
        elif target > inorder_arr[-1]:
            return inorder_arr[-1]
        while target > inorder_arr[i]:
            i += 1

        # if abs(inorder_arr[i] - target) < abs(inorder_arr[i - 1] - target):
        #     return inorder_arr[i]
        # else:
        #     return inorder_arr[i - 1]
        return min(inorder_arr[i - 1], inorder_arr[i],
                   key=lambda x: abs(target - x))


"""
Approach 2: Incomplete Inorder Traversal
Time Complexity: O(k), where k is index where target exits in sorted array
Space Complexity: O(h), h = height
"""
