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

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    """
    Linked list implementation
    """
    def __init__(self, double=False):
        self.head = None
        self.double = double

    def is_double(self):
        """
        Is the list single or doubly linked
        :return: boolean
        """
        return self.double

    def is_empty(self):
        return self.head == None

    def add_item(self, item):
        new_node = Node(item, double=self.double)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, searched_item):
        current_node = self.head
        found = None
        while current is not None and found is None:
            if current.data == searched_item:
                found = current
            else:
                current = current.next
        return found

    def remove(self, remove_item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == remove_item:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self.head = current.next
        else:
            previous.set_next(current.next)

    def show(self):
        """
        to do
        :return:
        """
        pass