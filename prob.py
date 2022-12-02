from player import Player
from typing import Dict
from candy_land import game
from game import Game
from card import Card

game_copy: Game = Game()

def compute_probabilities(player: Player) -> Dict[str, float]:
    probabilities: Dict[str, float]
    # get n probabilities:
        # n times:
            # get 1 probability:
                # play n random games
                # get the winner for each game
                # divide each by total number of games
    # compute their average
    # return that average

    return probabilities

def play_n_random_games() -> Dict[str, float]:
    probabilities: Dict[str, float]

    # n times:
        # play 1 random game:


    return probabilities

def play_random_game() -> int:
    pass
    # pick a random card from the deck

    # take a turn using that card