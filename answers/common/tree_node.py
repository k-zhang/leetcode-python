class TreeNode:

    def __init__(self, input_list):
        if len(input_list) == 0:
            raise ValueError("input_list cannot be empty")

        self.val = input_list[0]

        left = input_list[1: len(input_list) // 2 + 1]
        right = input_list[len(input_list) // 2 + 1:]
        
        self.left = TreeNode(left) if len(left) > 0 else None
        self.right = TreeNode(right) if len(right) > 0 else None
