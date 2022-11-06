from typing import List, Set
from Card import Card
from Player import Player

class GameState:
    def __init__(self, player_positions: List[int], discard_pile: Set[Card], curr_player: Player) -> None:
        self.player_positions = player_positions
        self.discard_pile = discard_pile
        self.curr_player = curr_player