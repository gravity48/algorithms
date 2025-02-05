from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = {0: 1}

        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            num_path = prefix_sum.get(current_sum - targetSum, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            num_path += dfs(node.left, current_sum)
            num_path += dfs(node.right, current_sum)
            prefix_sum[current_sum] -= 1
            return num_path

        return dfs(root, 0)
