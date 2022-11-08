from game import Game
from player import Player
from board_space import BoardSpace, Color, TreatSpace, Treat, Shortcut, ShortcutSpace
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
        Player(1, BoardSpace(Color.START, 0)),
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
            Player(1, BoardSpace(Color.BLUE, 30)),
            Player(2, BoardSpace(Color.START, 0)),
            Player(3, TreatSpace(Treat.CANDY_CANE)),
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
        Player(1, BoardSpace(Color.BLUE, 30)),
        Player(2, BoardSpace(Color.START, 0)),
        Player(3, TreatSpace(Treat.CANDY_CANE)),
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
        if players[i].player_number != correct_players[i].player_number or players[i].board_space.color != correct_players[i].board_space.color or correct_players[i].board_space.position != players[i].board_space.position:
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