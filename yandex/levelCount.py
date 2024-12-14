import sys

sys.setrecursionlimit(100000)


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.child = []
        self.is_parent = True


_hash = {}

with open('input.txt', 'rt') as f:
    count = int(f.readline()) - 1
    while count:
        child_val, parent_val = f.readline().replace('\n', '').split(' ')
        if parent_val not in _hash:
            _hash[parent_val] = TreeNode(parent_val)
        if child_val not in _hash:
            _hash[child_val] = TreeNode(child_val)
        parent = _hash[parent_val]
        child = _hash[child_val]
        child.is_parent = False
        parent.child.append(child)
        count -= 1


def dfs(node, count):
    if not node:
        return
    print(node.val, count)
    for child in node.child:
        dfs(child, count + 1)


root = None
for value in _hash.values():
    if value.is_parent:
        root = value
        break
dfs(root, 1)
