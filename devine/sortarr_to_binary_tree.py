from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        length = len(nums)

        def rec(left, right):
            if left > length - 1 or right < 0 or left > right:
                return None
            m = left + ((right - left) // 2)
            node = TreeNode(nums[m])
            node.left = rec(left=left, right=m - 1)
            node.right = rec(left=m + 1, right=right)
            return node

        median = len(nums) // 2
        root = TreeNode(nums[median])
        root.left = rec(left=0, right=median - 1)
        root.right = rec(left=median + 1, right=length - 1)
        return root


if __name__ == '__main__':
    Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
