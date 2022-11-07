from typing import Union
from game_state import GameState
from player import Player
from board import Board
from discard_pile import DiscardPile

class Game:
    def __init__(self, game_state: Union[GameState, None] = None) -> None:
        self.board: Board = Board()
        self.game_state: GameState
        if self.game_state is None:
            self.game_state = GameState([
                Player(1, self.board.board_spaces[0]),
                Player(2, self.board.board_spaces[0]),
                Player(3, self.board.board_spaces[0]),
                Player(4, self.board.board_spaces[0]),
            ], DiscardPile)
        else:
            self.game_state = game_state

        # self.deck: Deck = Deck(game_state.discard_pile)