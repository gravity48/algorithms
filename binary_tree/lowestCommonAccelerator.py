from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MySolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_depth_node = None

        def dfs(node, target):
            if not node:
                return False
            if node.val == target:
                return True
            return dfs(node.left, target) or dfs(node.right, target)

        def traversal_tree(node):
            if dfs(node, p.val) and dfs(node, q.val):
                nonlocal max_depth_node
                max_depth_node = node
                traversal_tree(node.left)
                traversal_tree(node.right)

        traversal_tree(root)
        return max_depth_node


class BestSolution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        LCA in a binary tree..
        Think of it like a single node, we need to find the p and q
        our search will be over when we find p in our right and q in our left
        or vice versa, at that point, the root is the answer!

        """
        # I have reached a dead end, I didn't find anything here
        if not root:
            return None

        # I see one of the targets! I will inform my caller!
        if root.val == q.val or root.val == p.val: return root

        # Look in the left, if you find p or q , return yourself
        foundInLeft = self.lowestCommonAncestor(root.left, p, q)

        # Look in the right, if you find p or q , return yourself
        foundInRight = self.lowestCommonAncestor(root.right, p, q)

        # Didnt find anything in the left, must be in right
        if not foundInLeft: return foundInRight

        # Didnt find anything in the right, must be in the left
        if not foundInRight: return foundInLeft

        # Found something in both! Hence this is the one!
        return root


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


if __name__ == '__main__':
    tree = construct_tree_from_arr([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    BestSolution().lowestCommonAncestor(tree, TreeNode(val=5), TreeNode(val=4))