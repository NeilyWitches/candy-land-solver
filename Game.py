from typing import Union
from GameState import GameState
from Player import Player
from Board import Board

class Game:
    def __init__(self, game_state: Union[GameState, None]=None) -> None:
        self.game_state = game_state
        self.player_one = Player(1)
        self.player_two = Player(2)
        self.player_three = Player(3)
        self.player_four = Player(4)
        if self.game_state is None:
            self.game_state = GameState([0, 0, 0, 0], {}, self.player_one)
        self.board = Board()