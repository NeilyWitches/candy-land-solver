from card import Card
from typing import Set, Dict, Union

class DiscardPile:
    def __init__(self, discarded_cards: Union[Set[Card], None] = None) -> None:
        if discarded_cards is None:
            discarded_cards = set()
            
        self.cards: Set[Card] = discarded_cards

    def add_card(self, card: Card) -> None:
        self.cards.add(card)