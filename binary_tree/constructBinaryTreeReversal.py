from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return

        def rec(values, indices):
            if not values:
                return
            root_value = values[-1]
            root = TreeNode(root_value)
            index = indices.index(root_value)
            root.left = rec(values[:index], indices[:index])
            root.right = rec(values[index: -1], indices[index + 1:])
            return root

        return rec(postorder, inorder)


if __name__ == '__main__':
    Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
