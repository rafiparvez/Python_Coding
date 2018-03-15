import collections
def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    '''
    named tuple to tell how namy of target nodes are present under ancestor
    ancestor field contains node if ancestor exists
    '''
    status = collections.namedtuple('status' ,('ancestor', 'num_target_nodes'))

    def helper(root, p, q):
        if not root:
            return status(None, 0)

        left_status = helper(root.left, p, q)

        if left_status.num_target_nodes == 2:
            return left_status  # found both nodes in left subtree

        right_status = helper(root.right, p, q)

        if right_status.num_target_nodes ==2:
            return right_status  # found both nodes in right subtree

        num_target_nodes = left_status.num_target_nodes + right_status.num_target_nodes + int(root in [p ,q])
        return status(root if num_target_nodes==2 else None ,num_target_nodes)

    return helper(root, p, q).ancestor

"""
Testing the code for following Binary Tree:

Constructed binary tree is
            A
          /  \
        B      C
      /  \    / \
    D     E  F    G

"""

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

A = Node(data='A')
B = Node(data='B')
C = Node(data='C')
D = Node(data='D')
E = Node(data='E')
F = Node(data='F')
G = Node(data='G')

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

print(lowestCommonAncestor(A, F, G).data)


'''
Approach 2: Iterative
'''
def lowestCommonAncestor2(root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q

print(lowestCommonAncestor2(A, F, G).data)
