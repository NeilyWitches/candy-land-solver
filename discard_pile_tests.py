from card import *
from board import *
from discard_pile import DiscardPile

def test_add_card() -> None:
    discard_pile: DiscardPile = DiscardPile()

    card_1: Card = Card(Color.BLUE)
    card_2: Card = Card(Color.GREEN, is_single_block=False)
    card_3: Card = TreatCard(Treat.CANDY_CANE)

    discard_pile.add_card(card_1)
    discard_pile.add_card(card_2)
    discard_pile.add_card(card_3)

    assert len(discard_pile.cards) == 3, "Discard pile has wrong number of cards"
    assert card_1 in discard_pile.cards, "The discard pile should contain card_1, but it does not"
    
def test_validate_discarded_cards() -> None:
    # returns true for an empty set
    assert DiscardPile.validate_discarded_cards(set()) == True, "an empty set of discarded cards should be valid, but it is not"

    # returns true for a valid discard pile
    assert DiscardPile.validate_discarded_cards({Card(Color.BLUE), TreatCard(Treat.CANDY_CANE), Card(Color.GREEN, is_single_block=False)}) == True, "A valid discard pile should come back valid, but it did not"

    # return false for an invalid discard pile
    assert DiscardPile.validate_discarded_cards({TreatCard(Treat.FROST), TreatCard(Treat.FROST)}) == False, "An discard pile with too many treat cards should come back invalid, but it did not"

def test_remove_card() -> None:
    card_1: Card = Card(Color.BLUE)
    card_2: Card = Card(Color.GREEN, is_single_block=False)
    card_3: Card = TreatCard(Treat.CANDY_CANE)

    discard_pile: DiscardPile = DiscardPile({ card_1, card_2, card_3})

    assert card_1 in discard_pile.cards, "card_1 should be in the discard pile but it is not"
    assert len(discard_pile.cards) == 3, "Discard pile has wrong number of cards before removal"
    
    discard_pile.remove_card(card_1)

    assert card_1 not in discard_pile.cards, "card_1 should not be in the discard pile after removal, but it is"
    assert len(discard_pile.cards) == 2, "Discard pile has the wrong number of cards after removal"