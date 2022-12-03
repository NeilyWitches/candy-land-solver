from card import *
from typing import Set
from board_space import *

class DiscardPile:
    def __init__(self) -> None:
        self.cards: Set[Card] = set()

    def add_card(self, card: Card) -> None:
        self.cards.add(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)

    def copy(self) -> 'DiscardPile':
        copy: DiscardPile = DiscardPile()
        for card in self.cards:
            if card.treat is not None:
                copy.add_card(TreatCard(card.treat))
            else:
                copy.add_card(Card(card.color, card.is_single_block))

        return copy