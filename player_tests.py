from player import Player
from board import Color, BoardSpace
from card import Card

def test_is_stuck() -> None:
    # if the player is on a sticky space and the card drawn does not unstick the player, they should be stuck
    player: Player = Player(1, BoardSpace(Color.YELLOW, 7, sticky=True), is_current_player=True)
    card: Card = Card(Color.BLUE)
    
    assert player.is_stuck(card) == True

    # if the player is on a sticky space but the card releases them they should be unstuck
    card = Card(Color.YELLOW)
    assert player.is_stuck(card) == False

    # should still work for a double block
    card.is_single_block = False
    assert player.is_stuck(card) == False

    # if the player is not on a sticky space they should be unstuck
    player.board_space = BoardSpace(Color.BLUE, 4)
    assert player.is_stuck(card) == False

def test_move_player() -> None:
    # it should move the player to the passed in board space
    origin_space: BoardSpace = BoardSpace(Color.RED, 1)
    destination_space: BoardSpace = BoardSpace(Color.PURPLE, 2)
    player: Player = Player(1, origin_space, is_current_player=True)
    player.move_player(destination_space)

    assert player.board_space == destination_space