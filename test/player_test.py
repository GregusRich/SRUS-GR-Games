import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    """
    Test cases for the Player class.
    """

    def test_uid_property(self):
        """
        Tests if the UID property returns the correct UID.
        """
        player = Player("1", "Alex")
        self.assertEqual(player.uid, "1")

    def test_name_property(self):
        """
        Tests if the name property returns the correct name.
        """
        player = Player("1", "Alex")
        self.assertEqual(player.name, "Alex")