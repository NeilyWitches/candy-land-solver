from typing import List, Set
from card import Card
from player import Player
from discard_pile import DiscardPile

class GameState:
    def __init__(self, players: List[Player], discard_pile: DiscardPile) -> None:
        self.players: List[Player] = players
        self.discard_pile: DiscardPile = discard_pile