
#perform level order traveresing and match root index and number of nodes traversed so far
# Time = O(n), Space = 0(2h) [max no. of nodes in queue]
def is_complete_iterative(root):
    print('****ITERATIVE****')
    queue=[]
    node_cnt = 0
    if root:
        queue.append((root,1))
    while len(queue)>0:
        node,index_cnt = queue.pop(0)
        node_cnt+=1
        if index_cnt > node_cnt:
            return False
        else:
            if node.left:
                queue.append((node.left, 2 * index_cnt))
            if node.right:
                queue.append((node.right, 2 * index_cnt +1))
    return True


def is_complete_recursive(tree):
    # This function checks if binary tree is complete or not
    def helper(root, index_cnt, node_cnt):

        # An empty is complete
        if root is None:
            return True

        node_cnt+=1
        # If index assigned to current nodes is more than
        # number of nodes in tree, then tree is not complete
        if index_cnt > node_cnt:
            return False

        # Recur for left and right subtress
        return (helper(root.left, 2 * index_cnt, node_cnt)
                and helper(root.right, 2 * index_cnt + 1, node_cnt)
                )
    return helper(tree, 1, 0)

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

print(is_complete_iterative(A))