from typing import Union
from game_state import GameState, GameStatePlayers
from player import Player
from board import Board
from discard_pile import DiscardPile
from board_space import BoardSpace
from deck import Deck

class Game:
    def __init__(self, game_state: Union[GameState, None] = None) -> None:
        self.board: Board = Board()
        self.game_state: GameState
        if game_state is None:
            starting_space: BoardSpace = self.board.board_spaces[0]
            self.game_state = GameState(GameStatePlayers(
                Player(1, starting_space),
                Player(2, starting_space),
                Player(3, starting_space),
                Player(4, starting_space),
            ), DiscardPile())
        else:
            self.game_state = game_state

        self.deck: Deck = Deck(self.game_state.discard_pile)