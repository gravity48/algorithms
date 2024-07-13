from typing import Optional, List


class TreeNode:

    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class BestSolution:

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return

        inorder_map = {val: index for index, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):

            if pre_start > pre_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            in_index = inorder_map[root_val]

            left_size = in_index - in_start

            root.left = build(pre_start + 1, pre_start + left_size, in_start, in_index - 1)

            root.right = build(pre_start + left_size + 1, pre_end, in_index + 1, in_end)

            return root
        return build(0, len(preorder) -1, 0, len(inorder) - 1)


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]):

        in_ordered_map = {value: index for index, value in enumerate(inorder)}

        if not preorder:
            return None

        def rec(values):
            if not values:
                return
            root = TreeNode(values[0])
            root_index = in_ordered_map[values[0]]
            left_values = list(filter(lambda x: in_ordered_map[x] < root_index, values))
            right_values = list(filter(lambda x: in_ordered_map[x] > root_index, values))
            root.left = rec(left_values)
            root.right = rec(right_values)
            return root
        return rec(preorder)


if __name__ == '__main__':
    Solution().buildTree([3, 9, 20, 15, 7], [9, 3,  15, 20, 7])
