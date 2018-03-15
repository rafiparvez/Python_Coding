def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if (max(p.val, q.val) < root.val):
        return lowestCommonAncestor(root.left, p, q)
    elif (min(p.val, q.val) > root.val):
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


'''
iterative
'''

def lowestCommonAncestor(self, root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root