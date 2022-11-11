from typing import Set, NamedTuple
from player import Player
from discard_pile import DiscardPile
from board import Color

class GameStatePlayers(NamedTuple):
    Player_1: Player
    Player_2: Player
    Player_3: Player
    Player_4: Player

class GameState:
    def __init__(self, players: GameStatePlayers, discard_pile: DiscardPile) -> None:
        num_current_players: int = 0
        for player in players:
            if player.is_current_player:
                num_current_players += 1
            if player.board_space.shortcut:
                raise ValueError("Cannot initialize game state with a player on a shortcut space")
            if player.board_space.color is Color.END:
                raise ValueError(f"Player {player.player_number} has already won this game")
        
        if num_current_players != 1:
            raise ValueError("There should be exactly one current player")
        
        self.players: GameStatePlayers = players
        self.discard_pile: DiscardPile = discard_pile