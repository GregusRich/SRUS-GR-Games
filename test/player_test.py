import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):

    def test_uid_property(self):
        player = Player("1", "Alex")
        print(f"Testing UID: {player.uid}")  # This line will print the uid to the console
        self.assertEqual(player.uid, "1")

    def test_name_property(self):
        player = Player("1", "Alex")
        print(f"Testing Name: {player.name}")  # This line will print the name to the console
        self.assertEqual(player.name, "Alex")
