class PlayerNode:
    """
    PlayerNode class acts as a node for a Player object in the double-linked list.

    Attributes:
        _player : The Player object that this node holds.
        _next   : Points to the next node in the list, None if this is the last node.
        _prev   : Points to the previous node in the list, None if this is the first node.
    """

    def __init__(self, player):
        """
        Initialise the node with the Player object and set next and previous pointers to None.

        Parameters:
            player : The Player object that this node will hold.
        """
        self._player = player
        self._next = None
        self._prev = None

    @property
    def player(self):
        """
        Returns the Player object that this node holds.

        :return: Player object
        """
        return self._player

    @property
    def next_node(self):
        """
        Returns the next node this node points to.

        :return: Next PlayerNode object or None
        """
        return self._next

    @next_node.setter
    def next_node(self, next_node):
        """
        Sets the next node this node should point to.

        :param next_node: Next PlayerNode object
        """
        self._next = next_node

    @property
    def prev_node(self):
        """
        Returns the previous node this node points to.

        :return: Previous PlayerNode object or None
        """
        return self._prev

    @prev_node.setter
    def prev_node(self, prev_node):
        """
        Sets the previous node this node should point to.

        :param prev_node: Previous PlayerNode object
        """
        self._prev = prev_node

    @property
    def key(self):
        """
        Returns the UID of the Player object that this node holds.

        :return: UID of the Player object.
        """
        return self._player.uid

    def __str__(self):
        """
        Returns a string representation of the PlayerNode.

        :return: String representation of this node, including the Player it holds
        """
        return f"PlayerNode: {self._player}"
