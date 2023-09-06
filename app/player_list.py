class PlayerList:
    """
    PlayerList class implements the double-linked list that manages PlayerNode objects.

    Attributes:
        head : Points to the first node in the list, None if the list is empty.
    """

    def __init__(self):
        """
        Initialise an empty list with the head pointing to None.
        """
        self.head = None
        self.tail = None


    def is_empty(self):
        """
        Checks if the list is empty.

        :return: True if empty, False otherwise.
        """
        return self.head is None

    def insert_at_head(self, new_node):
        """
        Inserts a new node at the head of the list.

        :param new_node: The new PlayerNode to insert.
        """
        if self.is_empty():
            self.head = new_node
            self.tail = new_node # The first node is both the head and the tail
        else:
            new_node._next = self.head  # Point the new node's next to the current head
            self.head._prev = new_node  # Point the current head's previous to the new node
            self.head = new_node  # Update the head to point to the new node

    def insert_at_tail(self, new_node):
        """
        Inserts a new node at the tail of the list.

        :param new_node: The new PlayerNode to insert.
        """
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node._prev = self.tail  # Point the new node's previous to the current tail
            self.tail._next = new_node  # Point the current tail's next to the new node
            self.tail = new_node  # Update the tail to point to the new node