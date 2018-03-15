def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    if not root:
        return None

    level = [root]

    result = []

    while (level):
        avg = sum([node.val for node in level]) / len(level)
        result.append(avg)
        new_level = []
        for node in level:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        level = new_level
    return result