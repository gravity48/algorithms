import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.childs = []
        self.is_parent = True


_hash = {}

with open('015', 'rt') as f:
    count = int(f.readline()) - 1
    while count:
        child_val, parent_val = f.readline().strip().split(' ')
        if child_val not in _hash:
            _hash[child_val] = TreeNode(child_val)
        if parent_val not in _hash:
            _hash[parent_val] = TreeNode(parent_val)
        parent = _hash[parent_val]
        child = _hash[child_val]
        parent.childs.append(child)
        child.is_parent = False
        count -= 1

root = None
for value in _hash.values():
    if value.is_parent:
        root = value
        break

results = []


@lru_cache()
def dfs(node):
    if not node:
        return 0
    count = sum(dfs(child) for child in node.childs)
    results.append([node.val, count])
    return count + 1


dfs(root)

results.sort(key=lambda x: x[0])

for res in results:
    print(res[0], res[1])
