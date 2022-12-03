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

def test_remove_card() -> None:
    card_1: Card = Card(Color.BLUE)
    card_2: Card = Card(Color.GREEN, is_single_block=False)
    card_3: Card = TreatCard(Treat.CANDY_CANE)

    discard_pile: DiscardPile = DiscardPile()
    discard_pile.add_card(card_1)
    discard_pile.add_card(card_2)
    discard_pile.add_card(card_3)

    assert card_1 in discard_pile.cards, "card_1 should be in the discard pile but it is not"
    assert len(discard_pile.cards) == 3, "Discard pile has wrong number of cards before removal"
    
    discard_pile.remove_card(card_1)

    assert card_1 not in discard_pile.cards, "card_1 should not be in the discard pile after removal, but it is"
    assert len(discard_pile.cards) == 2, "Discard pile has the wrong number of cards after removal"

def test_copy() -> None:
    original: DiscardPile = DiscardPile()
    original_card: Card = Card(Color.BLUE)
    original.add_card(original_card)
    assert original_card in original.cards, "The card should be in the original discard pile, but it isn't"
    copy: DiscardPile = original.copy()
    assert original != copy, "The copy should not be the same as the original, but it is"
    assert original_card not in copy.cards, "The card should not be in the copy discard pile, but it is"
    copy_card: Card
    for card in copy.cards:
        copy_card = card

    assert copy_card != original_card, "The copy card should not be the same as the original card, but it is"
    assert copy_card.color == original_card.color, "The color of the copy card should be the same as the original"
    assert copy_card.is_single_block == original_card.is_single_block, "The is single block attribute of the copy card should be the same as the original, but it is not"
    assert copy_card.treat == original_card.treat, "The treat of the copy card should be the same as the treat of the original, but it is not"

