from card import Card
from typing import Set, Dict, Union
from board_space import *

class DiscardPile:
    def __init__(self) -> None:
        self.cards: Set[Card] = set()

    def add_card(self, card: Card) -> None:
        self.cards.add(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)