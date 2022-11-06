from typing import List, Set
from Card import Card
from Player import Player

class GameState:
    def __init__(self, players: List[Player], discard_pile: Set[Card]) -> None:
        self.players: List[Player] = players
        self.discard_pile: Set[Card] = discard_pile