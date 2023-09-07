from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

if __name__ == "__main__":
    # Initialise an empty player list
    player_list = PlayerList()

    # Create player instances
    player1 = Player("1", "Joe")
    player2 = Player("2", "Gregus")
    player3 = Player("3", "Optimus")
    player4 = Player("4", "Tom")

    # Wrap them in PlayerNode instances
    node1 = PlayerNode(player1)
    node2 = PlayerNode(player2)
    node3 = PlayerNode(player3)
    node4 = PlayerNode(player4)

    # Add them to the list
    player_list.insert_at_head(node1)
    player_list.insert_at_head(node2)
    player_list.insert_at_head(node3)
    player_list.insert_at_head(node4)

    # Display the list
    player_list.display()

    # Display the list in reverse
    player_list.display(forward=False)
