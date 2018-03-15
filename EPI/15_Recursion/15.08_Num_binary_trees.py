class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def genrate_BTs(num_nodes):
    if num_nodes==0:
        return [None]

    result = []

    for left_nodes in range(num_nodes):
        right_nodes = num_nodes-left_nodes - 1

        left_trees = genrate_BTs(left_nodes)
        right_trees = genrate_BTs(right_nodes)

        for left_tree in left_trees:
            for right_tree in right_trees:
                result.append(TreeNode(0, left_tree, right_tree))
    return result


print(len(genrate_BTs(3)))





