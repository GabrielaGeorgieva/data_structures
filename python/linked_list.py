class Node(object):
    """
    Node class implementation.
    Node is one element of the linked list.
    May be single or double linked
    """
    def __init__(self, data, double=False):
        """

        :param data: int: data to store in the node
        :param double: boolean: True if doubly linked list
        :return:
        """
        self.data = data
        self.next = None
        if double:
            self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

