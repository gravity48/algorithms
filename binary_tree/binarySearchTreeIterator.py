def binary_tree_generator(node):
    if not node.left and not node.right:
        yield node
        return
    yield from binary_tree_generator(node.left)
    yield from binary_tree_generator(node.right)
    yield node
