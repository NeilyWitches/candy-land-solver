from typing import Set
from Card import Card

class Deck:
    def __init__(self, cards: Set[Card]) -> None:
        self.cards = cards
