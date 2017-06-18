class BinaryNode(object):
    def __init__(self, node):
        self.node = [node, [], []]

    def pop(self, i):
        return self.node.pop(i)

    def insert(self, index, value):
        return self.node.insert(index, value)


class SimpleBinaryTree(object):
    """
    Binary tree implementation using linked lists.
    Simple, because it does not have the binary tree property
    """

    def __init__(self, root):
        """
        Initialize binary tree with root
        :param root: int: value of the root
        :return:
        """
        self.root = BinaryNode(root)

    def insert_left(self, new_subtree):
        """
        Insert left branch on a node
        :param new_subtree: nested list
        :return:
        """
        old_left = self.root.pop(1)
        if len(old_left) > 1:
            self.root.insert(1, [new_subtree, old_left, []])
        self.root.insert(1, [new_subtree, [], []])
        return self.root

    def insert_right(self, new_subtree):
        old_left = self.root.pop(2)
        if len(old_left) > 1:
            self.root.insert(2, [new_subtree, [], old_left])
        else:
            self.root.insert(2, [new_subtree, [], []])
        return self.root

    def get_root(self):
        pass

    def set_root(self):
        pass

    def get_left(self):
        pass

    def get_right(self):
        pass
    