from typing import Union
from GameState import GameState
from Player import Player
from Board import Board
from BoardSpace import BoardSpace

class Game:
    def __init__(self, game_state: Union[GameState, None] = None) -> None:
        self.board: Board = Board()
        self.game_state: Union[GameState, None] = game_state
        if self.game_state is None:
            self.game_state = GameState([
                Player(1, self.board.board[0]),
                Player(2, self.board.board[0]),
                Player(3, self.board.board[0]),
                Player(4, self.board.board[0]),
            ], {})