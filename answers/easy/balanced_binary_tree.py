def is_balanced(root):
    if root is None:
        return True
    return dfs(root, 0) != -1


def dfs(root, depth):
    if root is None:
        return depth

    depth_left = dfs(root.left, depth + 1)
    depth_right = dfs(root.right, depth + 1)

    if depth_left == -1 or depth_right == -1:
        return -1

    return max(depth_left, depth_right) if abs(depth_left - depth_right) <= 1 else -1
