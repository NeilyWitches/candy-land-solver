from player import Player
from board_space import *
from card import Card
from game import Game

def test_is_stuck() -> None:
    # if the player is on a sticky space and the card drawn does not unstick the player, they should be stuck
    player: Player = Player(1, BoardSpace(Color.YELLOW, 7, sticky=True), is_current_player=True)
    card: Card = Card(Color.BLUE)
    
    assert player.is_stuck(card) == True, "The player should be stuck but they are not"

    # if the player is on a sticky space but the card releases them they should be unstuck
    card = Card(Color.YELLOW)
    assert player.is_stuck(card) == False, "The player should not be stuck, but they are"

    # should still work for a double block
    card.is_single_block = False
    assert player.is_stuck(card) == False, "The player should not be stuck, but they are"

    # if the player is not on a sticky space they should be unstuck
    player.board_space = BoardSpace(Color.BLUE, 4)
    assert player.is_stuck(card) == False, "The player should not be stuck, but they are"

def test_move_player() -> None:
    # it should move the player to the passed in board space
    origin_space: BoardSpace = BoardSpace(Color.RED, 1)
    destination_space: BoardSpace = BoardSpace(Color.PURPLE, 2)
    player: Player = Player(1, origin_space, is_current_player=True)
    player.move_player(destination_space)

    assert player.board_space == destination_space, "The player did not move to the correct board space"

def test_toggle_is_current_player() -> None:
    # if used on a player who is not the current player, makes them the current player
    not_curr_player: Player = Player(1, BoardSpace(Color.BLUE, 0))
    assert not_curr_player.is_current_player == False, "The player should not be the current player, but they are"
    not_curr_player.toggle_is_current_player()
    assert not_curr_player.is_current_player == True, "The player should be the current player, but they are not"

    # if used on a player who IS the current player, stops them from being current player
    curr_player: Player = Player(2, BoardSpace(Color.PURPLE, 20), is_current_player=True)
    assert curr_player.is_current_player == True, "The player should be the current player, but they are not"
    curr_player.toggle_is_current_player()
    assert curr_player.is_current_player == False, "The player should not be the current player, but they are"