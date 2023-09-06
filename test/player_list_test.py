import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):

    def test_insert_at_head_empty_list(self):
        """
        Test inserting a new node at the head of an empty list.
        """
        player_list = PlayerList()
        player = Player("1", "Alex")
        node = PlayerNode(player)

        player_list.insert_at_head(node)

        self.assertEqual(player_list.head, node)
        self.assertEqual(player_list.tail, node)
        self.assertIsNone(node.prev_node)
        self.assertIsNone(node.next_node)

    def test_insert_at_head_non_empty_list(self):
        """
        Test inserting a new node at the head of a non-empty list.
        """
        player_list = PlayerList()
        player1 = Player("1", "Alex")
        node1 = PlayerNode(player1)
        player_list.insert_at_head(node1)

        player2 = Player("2", "Bob")
        node2 = PlayerNode(player2)

        player_list.insert_at_head(node2)

        self.assertEqual(player_list.head, node2)
        self.assertEqual(player_list.tail, node1)
        self.assertEqual(node2.next_node, node1)
        self.assertEqual(node1.prev_node, node2)
        self.assertIsNone(node2.prev_node)

    def test_insert_at_tail_empty_list(self):
        """
        Test inserting a new node at the tail of an empty list.
        """
        player_list = PlayerList()
        player = Player("1", "Alex")
        node = PlayerNode(player)

        player_list.insert_at_tail(node)

        self.assertEqual(player_list.head, node)
        self.assertEqual(player_list.tail, node)
        self.assertIsNone(node.prev_node)
        self.assertIsNone(node.next_node)

    def test_insert_at_tail_non_empty_list(self):
        """
        Test inserting a new node at the tail of a non-empty list.
        """
        player_list = PlayerList()
        player1 = Player("1", "Alex")
        node1 = PlayerNode(player1)
        player_list.insert_at_head(node1)

        player2 = Player("2", "Bob")
        node2 = PlayerNode(player2)

        player_list.insert_at_tail(node2)

        self.assertEqual(player_list.head, node1)
        self.assertEqual(player_list.tail, node2)
        self.assertEqual(node1.next_node, node2)
        self.assertEqual(node2.prev_node, node1)
        self.assertIsNone(node1.prev_node)
        self.assertIsNone(node2.next_node)

    def test_delete_from_head(self):
        """
        Test deleting a node from the head of the list.
        """
        player_list = PlayerList()
        player1 = Player("1", "Alex")
        node1 = PlayerNode(player1)
        player_list.insert_at_head(node1)

        player_list.delete_from_head()

        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)

    def test_delete_from_tail(self):
        """
        Test deleting a node from the tail of the list.
        """
        player_list = PlayerList()
        player1 = Player("1", "Alex")
        node1 = PlayerNode(player1)
        player_list.insert_at_head(node1)

        player_list.delete_from_tail()

        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)