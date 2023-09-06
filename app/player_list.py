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
