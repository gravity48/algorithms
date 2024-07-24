from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree_from_arr(arr_):
    if not arr_:
        return
    root = TreeNode(arr_[0])
    index = 1
    length = len(arr_)
    queue = deque()
    queue.append(root)
    while index < length:
        node = queue.popleft()
        node.left = TreeNode(arr_[index]) if arr_[index] else None
        node.right = TreeNode(arr_[index + 1]) if arr_[index + 1] else None
        queue.append(node.left)
        queue.append(node.right)
        index = index + 2
    return root


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def dfs(node):
            if not node:
                return
            dummy = node
            right = node.right
            left = node.left
            if left:
                node.right = dfs(left)
                while node.right:
                    node = node.right
            if right:
                node.right = dfs(right)
                node = node.right
            dummy.left = None
            return dummy

        return dfs(root)


class BestSolution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right  # We go to left Subtree's rightMost Node

                prev.right = cur.right  # We make current Node's right Subtree prev's right Subtree
                cur.right = cur.left  # We make it right Subtree
                cur.left = None  # Removing left

            cur = cur.right


if __name__ == '__main__':
    root = construct_tree_from_arr([1, 2, 5, 3, 4, None, 6])
    BestSolution().flatten(root)
