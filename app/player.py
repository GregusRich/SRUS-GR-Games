class Player:
    """
    Represents a Player with a unique ID and a name.
    """

    def __init__(self, uid: str, name: str):
        """
        Initializes the Player with the given uid and name.
        """
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        """
        Returns the unique identifier of the Player.

        :return: UID of the Player
        """
        return self._uid

    @property
    def name(self) -> str:
        """
        Returns the name of the Player.

        :return: Name of the Player
        """
        return self._name

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Player.

        :return: String representation of the Player
        """
        return f"Player {self._name} with UID {self._uid}"