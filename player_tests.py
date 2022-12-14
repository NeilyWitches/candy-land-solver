from player import Player
from board_space import *
from card import Card
from game import Game
from typing import List
from board import Board

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

def test_shortcut_taken() -> None:
    game: Game = Game()

    orange_card: Card
    other_cards: List[Card] = []
    for card in game.deck.cards:
        if card.color == Color.ORANGE and card.is_single_block:
            orange_card = card
            break

    other_card_count: int = 0
    for card in game.deck.cards:
        if card.color != Color.ORANGE:
            other_cards.append(card)
            other_card_count += 1
            if other_card_count == 4:
                break

    assert game.players.Player_1.shortcut_taken == None, "The current player has not yet taken the shortcut so their shortcut taken attr should be None"
    game.take_turn(orange_card)
    assert game.players.Player_1.board_space == game.board.board_spaces.PurpleSpace_9, "The player should be on purple 9, but they are not"
    assert game.players.Player_1.shortcut_taken == Shortcut.RAINBOW_TRAIL, "Player 1 just took a shortcut, but their shortcut_taken attribute does not reflect that"

    for card in other_cards:
        game.take_turn(card)

    for player in game.players:
        assert player.shortcut_taken == None, "Every player should not have just taken a shortcut, but at least one of them did"

def test_update_shortcut_taken() -> None:
    player: Player = Player(1, BoardSpace(Color.START, 0))
    assert player.shortcut_taken == None, "took shortcut should be None, but it is not None"
    player.update_shortcut_taken(Shortcut.GUMDROP_PASS)
    assert player.shortcut_taken == Shortcut.GUMDROP_PASS, "took shortcut should be gumdrop pass, but it is not"
    player.update_shortcut_taken(Shortcut.RAINBOW_TRAIL)
    assert player.shortcut_taken == Shortcut.RAINBOW_TRAIL, "took shortcut should be rainbow trail, but it is not"

def test_copy() -> None:
    original: Player = Player(1, BoardSpace(Color.BLUE, 0))
    copy: Player = original.copy(Board())
    assert original != copy, "The original should not be equal to the copy, but it is"
    assert original.player_number == copy.player_number, "The original's player number should be equal to the copy's player number, but it isn't"
    assert original.board_space != copy.board_space, "The original's board space should not be equal to the copy's board space, but it is"
    assert original.board_space.color == copy.board_space.color, "The original's board space's color should be the same as the copy's color, but it isn't"
    assert original.board_space.position == copy.board_space.position, "The original's board space's position should be the same as the copy's position, but it isn't"
    assert original.board_space.sticky == copy.board_space.sticky, "The original's board space's sticky should be the same as the copy's sticky, but it isn't"
    assert original.board_space.treat == copy.board_space.treat, "The original's board space's treart should be the same as the copy's treat"
    assert original.is_current_player == copy.is_current_player, "The original's is current player attribute should be equal to the copy's is current player attribute, but it is not"
    assert original.shortcut_taken == copy.shortcut_taken, "The original's shortcut taken attribute should be equal to the copy's shortcut taken attribute, but it is not"
    assert original.stuck_state == copy.stuck_state, "The original's stuck_state attribute should be the same as the copy's but it is not"