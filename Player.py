from board_space import *
from card import Card

class Player:
    def __init__(self, player_number: int, board_space: BoardSpace, is_current_player: bool = False) -> None:
        self.player_number: int = player_number
        self.board_space: BoardSpace = board_space
        self.is_current_player: bool = is_current_player
        self.took_shortcut: bool = False

    def is_stuck(self, card: Card) -> bool:
        if not self.is_current_player:
            raise ValueError("Should only be checking if the CURRENT player is stuck")

        if not self.board_space.sticky:
            return False
        
        if self.board_space.color == card.color:
            return False

        return True

    def move_player(self, board_space: BoardSpace) -> None:
        # only move the player if they are the current player
        if not self.is_current_player:
            raise ValueError("Can only move the current player")

        self.board_space = board_space

    def toggle_is_current_player(self) -> None:
        self.is_current_player = not self.is_current_player

    def toggle_took_shortcut(self, took_shortcut: bool) -> None:
        self.took_shortcut = took_shortcut