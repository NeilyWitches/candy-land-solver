from card import *
from board import *
from discard_pile import DiscardPile

def test_add_card() -> None:
    discard_pile: DiscardPile = DiscardPile()

    card_1 = Card(Color.BLUE)
    card_2 = Card(Color.GREEN, is_single_block=False)
    card_3 = TreatCard(Treat.CANDY_CANE)

    discard_pile.add_card(card_1)
    discard_pile.add_card(card_2)
    discard_pile.add_card(card_3)

    assert len(discard_pile.cards) == 3, "Discard pile has wrong number of cards"
    
def test_validate_discarded_cards() -> None:
    # returns true for an empty set
    assert DiscardPile.validate_discarded_cards(set()) == True, "an empty set of discarded cards should be valid, but it is not"

    # returns true for a valid discard pile
    assert DiscardPile.validate_discarded_cards({Card(Color.BLUE), TreatCard(Treat.CANDY_CANE), Card(Color.GREEN, is_single_block=False)}) == True, "A valid discard pile should come back valid, but it did not"

    # return false for an invalid discard pile
    assert DiscardPile.validate_discarded_cards({TreatCard(Treat.FROST), TreatCard(Treat.FROST)}) == False, "An discard pile with too many treat cards should come back invalid, but it did not"