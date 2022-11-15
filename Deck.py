from typing import Set
from card import *
from discard_pile import DiscardPile
from board import *

class Deck:
    def __init__(self, discard_pile: DiscardPile) -> None:
        self.cards: Set[Card] = self.generate_deck(discard_pile)

    def generate_deck(self, discard_pile: DiscardPile) -> Set[Card]:
        discarded_cards = discard_pile.cards.copy()
        cards: Set[Card] = set()

        def make_several_cards(is_single_block: bool, color: Color, quantity: int) -> None:
            for i in range(quantity):
                removed: bool = False
                for card in discarded_cards:
                    if card.color is color and card.is_single_block is is_single_block:
                        discarded_cards.remove(card)
                        removed = True
                        break
                if not removed:
                    cards.add(Card(color, is_single_block))

        def make_treat_card(treat: Treat) -> None:
            removed: bool = False
            for card in discarded_cards:
                if card.treat is treat:
                    discarded_cards.remove(card)
                    removed = True
                    break
            if not removed:
                cards.add(TreatCard(treat))
            
        make_several_cards(True, Color.RED, 6)
        make_several_cards(False, Color.RED, 4)
        make_several_cards(True, Color.ORANGE, 6)
        make_several_cards(False, Color.ORANGE, 3)
        make_several_cards(True, Color.YELLOW, 6)
        make_several_cards(False, Color.YELLOW, 4)
        make_several_cards(True, Color.GREEN, 6)
        make_several_cards(False, Color.GREEN, 3)
        make_several_cards(True, Color.BLUE, 6)
        make_several_cards(False, Color.BLUE, 4)
        make_several_cards(True, Color.PURPLE, 6)
        make_several_cards(False, Color.PURPLE, 4)

        make_treat_card(Treat.PLUMB)
        make_treat_card(Treat.CANDY_CANE)
        make_treat_card(Treat.GUMDROP)
        make_treat_card(Treat.LOLLIPOP)
        make_treat_card(Treat.NUT)
        make_treat_card(Treat.FROST)

        return cards