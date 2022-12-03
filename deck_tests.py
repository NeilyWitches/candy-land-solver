from board import *
from deck import Deck
from typing import Dict, Union, Set
from card import *
from discard_pile import DiscardPile

def test_generate_deck() -> None:
    # empty discard pile
    discard_pile: DiscardPile = DiscardPile()

    deck: Deck = Deck()
    # the generated deck should be complete
    assert is_complete(deck) == True, "Deck should be complete"

def is_complete(deck: Deck):
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
        Treat.PLUM: 0,
        Treat.CANDY_CANE: 0,
        Treat.GUMDROP: 0,
        Treat.LOLLIPOP: 0,
        Treat.NUT: 0,
        Treat.FROST: 0,
    }

    def count_cards_in(pile: Set[Card]) -> None:
        for card in pile:
            if card.treat:
                if card.treat is Treat.PLUM:
                    counter[Treat.PLUM] += 1
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
        Treat.PLUM: counter[Treat.PLUM] == 1,
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


def test_draw_card() -> None:
    # removes a card from the deck
    deck: Deck = Deck()
    card_to_be_removed: Card
    for card in deck.cards:
        card_to_be_removed = card
        break

    assert card_to_be_removed in deck.cards, "The card should be in the deck, but it is not"

    deck.draw_card(card_to_be_removed)

    assert card_to_be_removed not in deck.cards, "The card should have been removed from the deck, but it was not"

def test_find_card() -> None:
    # should find the right card, double block
    user_input: str = "pp"
    deck: Deck = Deck()
    card: Card = deck.find_card(user_input)

    assert card.is_single_block == False, "The card should be a double block card, but it is not"
    assert card.color == Color.PURPLE, "The card should be purple, but it is not"
    assert card.treat == None, "The card should not be a treat card, but it is"

    # should find the right card, single block
    user_input = "b"
    card = deck.find_card(user_input)

    assert card.is_single_block == True, "The card should be single block, but it isn't"
    assert card.color == Color.BLUE, "The card should be blue, but it is not"
    assert card.treat == None, "The card should not be a treat card, but it is"

    # should find the right card, treat
    user_input = "nut"
    card = deck.find_card(user_input)

    assert card.is_single_block == True, "The card should be a single block card, but it isn't"
    assert card.color == Color.PINK, "The card should be pink, but it is not"
    assert card.treat == Treat.NUT, "The treat on the card should be the nut, but it is not"

def test_copy() -> None:
    original: Deck = Deck()
    copy: Deck = original.copy()
    card: Card = original.find_card("r")
    assert card in original.cards, "The card should be in the original, but it is not"
    assert card not in copy.cards, "The card should not be in the copy, but it is"
    original.draw_card(card)
    copy = original.copy()
    assert len(copy.cards) == len(original.cards), "The two decks should have the same length, but they do not"
    assert original != copy, "The 2 decks should have different addresses in memory, but they do not"
    assert card not in original.cards, "The card should have been removed from the original deck, but it was not"
    assert card not in copy.cards, "The card should not be in the copy"