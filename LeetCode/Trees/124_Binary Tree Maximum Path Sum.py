# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Complexity Analysis

Time complexity : O(N) where N is number of nodes, since we visit each node not
  more than 2 times.
Space complexity : O(log(N). We have to keep a recursion stack of the size of
the tree height, which is O(log(N)) for the binary tree.

"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
        '''

        self.max_path_sum = float('-inf')

        def max_path_helper(root):
            if not root:
                return 0

            left_gain = max_path_helper(root.left)
            right_gain = max_path_helper(root.right)

            '''
            This includes the case, when max path could pass through the
            node, but root node of max path could be some other ancestor
            of this node
            '''
            max_single = max(root.val,
                             root.val + max(left_gain, right_gain))

            '''
            This is the case when current root is root of the max path 
            and max path contains none of its ancestors
            '''
            max_top = max(max_single, root.val + left_gain + right_gain)

            self.max_path_sum = max(self.max_path_sum, max_top)

            return max_single

        max_path_helper(root)
        return self.max_path_sum
