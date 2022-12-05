from typing import Dict, List
from card import Card
import random
from board_space import Color

def compute_probabilities(n: int, game) -> List[float]:
    probabilities: List[float] = play_n_random_games(100, game)
    for _ in range(n - 1):
        results: List[float] = play_n_random_games(100, game)
        probabilities = [a+b for a, b in zip(results, probabilities)]

    return list(map(lambda probability: probability / n, probabilities))

def play_n_random_games(n: int, game) -> List[float]:
    wins: List[int] = [0, 0, 0, 0]
    for _ in range(n):
        game_copy = game.copy()
        results: List[int] = play_random_game(game_copy)
        wins = [a+b for a, b in zip(wins, results)]

    return list(map(lambda win: win / n, wins))

def play_random_game(game_copy) -> List[int]:
    # until game over:
    while not game_copy.is_game_over():
        # pick a random card from the deck
        random_card: Card = random.choice(tuple(game_copy.deck.cards))
        # take a turn using that card
        game_copy.take_turn(random_card)

    return [
        1 if game_copy.players.Player_1.board_space.color == Color.END else 0,
        1 if game_copy.players.Player_2.board_space.color == Color.END else 0,
        1 if game_copy.players.Player_3.board_space.color == Color.END else 0,
        1 if game_copy.players.Player_4.board_space.color == Color.END else 0,
    ]