class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This construct a tree structure from a list
# An None in the list indicates the node is not existence.
# The layout
#               1
#           /      \
#          2        3
#        /   \    /   \
#       4     5  6     7
# It can be used to construct unbalanced tree
#     [1, 2, 3, None, None, 4, 5]
#              1
#           /     \
#          2       3
#                /   \
#               4     5
def construct_tree(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        if nums[0] is None:
            raise ValueError("Cannot have one single null as input.")
        return TreeNode(nums[0])

    tree = []
    for num in nums:
        node = TreeNode(num) if num is not None else None
        tree.append(node)

    index = 0
    search = 1
    while search < len(tree):
        node = tree[index]
        if node is not None:
            node.left = tree[search]
            search += 1
            if search < len(tree):
                node.right = tree[search]
                search += 1
        index += 1

    return tree[0]


# This will construct tree in different layout than the last one
# An None in the list indicates the data is None but the not still exists.
#               1
#           /      \
#          2        5
#        /   \    /   \
#       3     4  6     7
# This cannot be used to construct unbalanced tree construct tree in different layout than the last one
#     [1, 2, 3, None, None, 4, 5]
#               1
#           /      \
#          2        None
#        /   \      /   \
#       3    None  6     7
def construct_tree_new(input_list):
    if len(input_list) == 0:
        raise ValueError("input_list cannot be empty")

    node = TreeNode(input_list[0])

    left = input_list[1: len(input_list) // 2 + 1]
    right = input_list[len(input_list) // 2 + 1:]

    node.left = construct_tree_new(left) if len(left) > 0 else None
    node.right = construct_tree_new(right) if len(right) > 0 else None

    return node


def depth_first_traversal(node, depth=0):
    if node is not None:
        # Print the current node value with appropriate indentation
        print("  " * depth + str(node.val))
        # Traverse the left subtree with increased depth
        depth_first_traversal(node.left, depth + 1)
        # Traverse the right subtree with increased depth
        depth_first_traversal(node.right, depth + 1)
