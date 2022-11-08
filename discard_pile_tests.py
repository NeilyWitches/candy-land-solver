from card import Card, TreatCard
from board_space import Color, Treat
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