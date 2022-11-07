from board_space import Treat, Color
from deck import Deck
from typing import Dict, Union, Set
from card import Card, TreatCard
from discard_pile import DiscardPile

def test_generate_deck() -> None:
    # empty discard pile
    discard_pile: DiscardPile = DiscardPile()

    deck: Deck = Deck(discard_pile)
    # For an empty discard pile, the generated deck should be complete with or without the discard pile
    assert is_complete(deck, discard_pile) == True, "Deck is not complete with an empty discard pile"
    assert is_complete(deck) == True, "Deck is not complete without an empty discard pile"

    # For non-empty discard pile,
    card_1: Card = Card(Color.BLUE)
    card_2: Card = Card(Color.GREEN, is_single_block=False)
    card_3: Card = TreatCard(Treat.CANDY_CANE)

    discard_pile.add_card(card_1)
    discard_pile.add_card(card_2)
    discard_pile.add_card(card_3)

    # the generated deck + discard pile is too many cards
    assert is_complete(deck, discard_pile) == False, "Deck should have too many cards"

    # create a new deck using the new discard pile
    deck = Deck(discard_pile)

    # the generated deck is only complete WITH the discard pile
    assert is_complete(deck, discard_pile) == True, "Deck is not complete with a discard pile"
    assert is_complete(deck) == False, "Deck is complete without a discard pile"

def is_complete(deck: Deck, discard_pile = DiscardPile()):
    counter: Dict[Union[str, Treat], int] = {
        "single_block_red": 0,
        "double_block_red": 0,
        "single_block_orange": 0,
        "double_block_orange": 0,
        "single_block_yellow": 0,
        "double_block_yellow": 0,
        "single_block_green": 0,
        "double_block_green": 0,
        "single_block_blue": 0,
        "double_block_blue": 0,
        "single_block_purple": 0,
        "double_block_purple": 0,
        Treat.PLUMB: 0,
        Treat.CANDY_CANE: 0,
        Treat.GUMDROP: 0,
        Treat.LOLLIPOP: 0,
        Treat.NUT: 0,
        Treat.FROST: 0,
    }

    def count_cards_in(pile: Set[Card]) -> None:
        for card in pile:
            if card.treat:
                if card.treat is Treat.PLUMB:
                    counter[Treat.PLUMB] += 1
                if card.treat is Treat.CANDY_CANE:
                    counter[Treat.CANDY_CANE] += 1
                if card.treat is Treat.GUMDROP:
                    counter[Treat.GUMDROP] += 1
                if card.treat is Treat.LOLLIPOP:
                    counter[Treat.LOLLIPOP] += 1
                if card.treat is Treat.NUT:
                    counter[Treat.NUT] += 1
                if card.treat is Treat.FROST:
                    counter[Treat.FROST] += 1
            else:
                if card.is_single_block:
                    if card.color is Color.RED:
                        counter["single_block_red"] += 1
                    if card.color is Color.PURPLE:
                        counter["single_block_purple"] += 1
                    if card.color is Color.YELLOW:
                        counter["single_block_yellow"] += 1
                    if card.color is Color.BLUE:
                        counter["single_block_blue"] += 1
                    if card.color is Color.ORANGE:
                        counter["single_block_orange"] += 1
                    if card.color is Color.GREEN:
                        counter["single_block_green"] += 1
                else:
                    if card.color is Color.RED:
                        counter["double_block_red"] += 1
                    if card.color is Color.PURPLE:
                        counter["double_block_purple"] += 1
                    if card.color is Color.YELLOW:
                        counter["double_block_yellow"] += 1
                    if card.color is Color.BLUE:
                        counter["double_block_blue"] += 1
                    if card.color is Color.ORANGE:
                        counter["double_block_orange"] += 1
                    if card.color is Color.GREEN:
                        counter["double_block_green"] += 1

    count_cards_in(deck.cards)
    count_cards_in(discard_pile.cards)

    check_list: Dict[Union[str, Treat], bool] = {
        "single_block_red": counter["single_block_red"] == 6,
        "double_block_red": counter["double_block_red"] == 4,
        "single_block_orange": counter["single_block_orange"] == 6,
        "double_block_orange": counter["double_block_orange"] == 3,
        "single_block_yellow": counter["single_block_yellow"] == 6,
        "double_block_yellow": counter["double_block_yellow"] == 4,
        "single_block_green": counter["single_block_green"] == 6,
        "double_block_green": counter["double_block_green"] == 3,
        "single_block_blue": counter["single_block_blue"] == 6,
        "double_block_blue": counter["double_block_blue"] == 4,
        "single_block_purple": counter["single_block_purple"] == 6,
        "double_block_purple": counter["double_block_purple"] == 4,
        Treat.PLUMB: counter[Treat.PLUMB] == 1,
        Treat.CANDY_CANE: counter[Treat.CANDY_CANE] == 1,
        Treat.GUMDROP: counter[Treat.GUMDROP] == 1,
        Treat.LOLLIPOP: counter[Treat.LOLLIPOP] == 1,
        Treat.NUT: counter[Treat.NUT] == 1,
        Treat.FROST: counter[Treat.FROST] == 1,
    }
    
    for item in check_list:
        if not check_list[item]:
            return False

    return True