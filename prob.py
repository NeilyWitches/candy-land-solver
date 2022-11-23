# given a game state, calculate each player's probability of winning
from test_game import TestGame
from board_space import Color
from player import Player
from candy_land import game
from typing import Dict
from game import Game
from board_space import BoardSpace

test_game = TestGame()
total: Dict[str, int] = {"games": 0}
game_copy: Game = Game(game.game_state)

def test_prob():
    if test_game.test_players[0].board_space.color == Color.END:
        total["games"] += 1
        return 1

    if test_game.test_players[1].board_space.color == Color.END:
        total["games"] += 1
        return 0

    wins = 0
    for card in test_game.test_deck:
        if card not in test_game.test_discard_pile:
            board_space_before = test_game.current_test_player().board_space
            test_game.take_test_turn(card)
            wins += test_prob()
            test_game.undo_test_turn(board_space_before, card)

    return wins

# print("prob: ", test_prob())
# print("total games: ", total["games"])

def win_probability(player: Player) -> float:
    if game_copy.is_game_over():
        total["games"] += 1
        return 1 if player.board_space.color == Color.END else 0
    
    wins: int = 0
    for card in game_copy.deck.cards:
        if card not in game.discard_pile.cards:
            board_space_before: BoardSpace = game_copy.current_player().board_space
            game_copy.simulate_turn(card)
            wins += win_probability(player)
            game_copy.undo_turn(board_space_before, card)