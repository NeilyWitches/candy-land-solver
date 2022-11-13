from game import Game
from player import Player
from board import BoardSpace, Color, TreatSpace, Treat
from game_state import GameState, GameStatePlayers
from discard_pile import DiscardPile
from card import Card, TreatCard
from typing import Set

def test_new_game() -> None:
    # creating a new game without a game state, initializes the game
    # with the correct game state
    game: Game = Game()
    game_state: GameState = game.game_state

    players: GameStatePlayers = game_state.players
    discard_pile: DiscardPile = game_state.discard_pile

    correct_players: GameStatePlayers = GameStatePlayers(
        Player(1, BoardSpace(Color.START, 0), is_current_player=True),
        Player(2, BoardSpace(Color.START, 0)),
        Player(3, BoardSpace(Color.START, 0)),
        Player(4, BoardSpace(Color.START, 0)),
    )
    correct_discard_pile: DiscardPile = DiscardPile(set())

    assert has_correct_players(players, correct_players) == True, "The game state has incorrect players"
    assert has_correct_discard_pile(discard_pile, correct_discard_pile) == True, "The game state has an incorrect discard pile"

    # creating a new game with a game state, initializes the game
    # with the correct game state
    game_state = GameState(
        GameStatePlayers(
            Player(1, BoardSpace(Color.BLUE, 3)),
            Player(2, BoardSpace(Color.START, 0)),
            Player(3, TreatSpace(Treat.CANDY_CANE), is_current_player=True),
            Player(4, BoardSpace(Color.PURPLE, 15)),
        ),
        DiscardPile({
            Card(Color.PURPLE), 
            Card(Color.ORANGE, is_single_block=False), 
            TreatCard(Treat.FROST)
        })
    )
    game = Game(game_state)
    game_state = game.game_state

    players = game_state.players
    discard_pile = game_state.discard_pile

    correct_players = GameStatePlayers(
        Player(1, BoardSpace(Color.BLUE, 3)),
        Player(2, BoardSpace(Color.START, 0)),
        Player(3, TreatSpace(Treat.CANDY_CANE), is_current_player=True),
        Player(4, BoardSpace(Color.PURPLE, 15)),
    )
    correct_discard_pile = DiscardPile({
        Card(Color.PURPLE),
        Card(Color.ORANGE, is_single_block=False),
        TreatCard(Treat.FROST)
    })

    assert has_correct_players(players, correct_players) == True, "The game state has incorrect players"
    assert has_correct_discard_pile(discard_pile, correct_discard_pile) == True, "The game state has an incorrect discard pile"

def has_correct_players(players: GameStatePlayers, correct_players: GameStatePlayers) -> bool:
    for i in range(0, 4):
        if players[i].player_number != correct_players[i].player_number or players[i].board_space.color != correct_players[i].board_space.color or correct_players[i].board_space.position != players[i].board_space.position or correct_players[i].is_current_player != players[i].is_current_player:
            return False
    return True

def has_correct_discard_pile(discard_pile: DiscardPile, correct_discard_pile: DiscardPile) -> bool:
    if len(discard_pile.cards) != len(correct_discard_pile.cards):
        return False

    bucket: Set = set()
    for card in discard_pile.cards:
        for correct_card in correct_discard_pile.cards:
            if correct_card not in bucket and card.is_single_block == correct_card.is_single_block and card.color == correct_card.color and card.treat == correct_card.treat:
                bucket.add(correct_card)

    return len(bucket) == len(discard_pile.cards)    

def test_game_over_check() -> None:
    # it should know the game is not over when none of the players 
    # have made it to the end yet

    game: Game = Game()
    game_over = game.check_if_game_over()

    assert game_over == False, "The game is not over"

    # apply drawn cards until someone wins a game
    # game.change_game_state()

def test_move_curr_player_to_treat() -> None:
    # only the current player should be moved
    game: Game = Game()
    current_player: Player = game.current_player()
    player_2: Player = game.players.Player_2
    player_3: Player = game.players.Player_3
    # make sure the current player is not player 2
    assert player_2 != current_player, "The current player is player 2"
    # all of the players start at the same board space, i.e. the start space
    assert current_player.board_space == player_2.board_space, "The current player and player 2 did not start at the same board space"
    # after the current player has been moved,
    game.move_curr_player_to_treat(TreatCard(Treat.CANDY_CANE))
    # the current player and player 2 should not be on the same board space
    assert current_player.board_space != player_2.board_space, "The current player and player 2 are on the same board space"
    # but player 2 and player 3 should still be on the start space
    assert player_2.board_space == player_3.board_space, "Player 2 and Player 3 are on different spaces"
    assert player_3.board_space == game.board.board_spaces.StartSpace, "Player 3 is not on the start space"

    # the current player should be moved to the correct treat space
    assert current_player.board_space == game.board.board_spaces.CandyCane, "The current player is on the wrong board space"

# def test_apply_drawn_card() -> None:


def test_current_player() -> None:
    # finds the current player
    game: Game = Game()
    current_player = game.game_state.players.Player_1

    assert game.current_player() == current_player

def test_move_curr_player_to_next():
    # it should move the current_player and not some other player
    game: Game = Game()
    current_player: Player = game.players.current_player()
    current_player.move_player(game.board.board_spaces.BoardSpace_1)
    other_player: Player = game.players.Player_2
    curr_player_board_space_before: BoardSpace = current_player.board_space
    other_player_board_space_before: BoardSpace = other_player.board_space

    game.move_curr_player_to_next(Color.BLUE)

    curr_player_board_space_after: BoardSpace = current_player.board_space
    other_player_board_space_after: BoardSpace = other_player.board_space

    assert other_player_board_space_before == other_player_board_space_after, "A player that was not the current player was moved"
    assert curr_player_board_space_before != curr_player_board_space_after, "The current player did not move"

    # it should move the current_player to the next board space of the correct color
    assert curr_player_board_space_after.color == Color.BLUE, "The player moved to the wrong color"

    # it should not move backwards
    assert curr_player_board_space_after.position > curr_player_board_space_before.position, "The player moved backwards"

    # it should not skip the color
    # assert 

    # the current player should not have stayed in the same spot
    # especially if they were on that color