from card import Card
from typing import Set, Dict, Union
from board_space import *

class DiscardPile:
    def __init__(self, discarded_cards: Union[Set[Card], None] = None) -> None:
        is_valid: bool = False
        if discarded_cards is None:
            is_valid = True
        else:
            is_valid = DiscardPile.validate_discarded_cards(discarded_cards)
        
        if not is_valid:
            raise ValueError("Invalid discard pile")

        if discarded_cards is None:
            discarded_cards = set()
            
        self.cards: Set[Card] = discarded_cards

    def add_card(self, card: Card) -> None:
        self.cards.add(card)

    @staticmethod
    def validate_discarded_cards(discarded_cards: Set[Card]) -> bool:
        counter: Dict[str, int] = {
            "red single": 0,
            "red double": 0,
            "orange single": 0,
            "orange double": 0,
            "yellow single": 0,
            "yellow double": 0,
            "green single": 0,
            "green double": 0,
            "blue single": 0,
            "blue double": 0,
            "purple single": 0,
            "purple double": 0,
            "plumb": 0,
            "candy cane": 0,
            "gumdrop": 0,
            "lollipop": 0,
            "nut": 0,
            "frost": 0,
        }

        for card in discarded_cards:
            if card.color == Color.RED and card.is_single_block:
                counter["red single"] += 1
            if card.color == Color.RED and not card.is_single_block:
                counter["red double"] += 1
            if card.color == Color.ORANGE and card.is_single_block:
                counter["orange single"] += 1
            if card.color == Color.ORANGE and not card.is_single_block:
                counter["orange double"] += 1
            if card.color == Color.YELLOW and card.is_single_block:
                counter["yellow single"] += 1
            if card.color == Color.YELLOW and not card.is_single_block:
                counter["yellow double"] += 1
            if card.color == Color.GREEN and card.is_single_block:
                counter["green single"] += 1
            if card.color == Color.GREEN and not card.is_single_block:
                counter["green double"] += 1
            if card.color == Color.BLUE and card.is_single_block:
                counter["blue single"] += 1
            if card.color == Color.BLUE and not card.is_single_block:
                counter["blue double"] += 1
            if card.color == Color.PURPLE and card.is_single_block:
                counter["purple single"] += 1
            if card.color == Color.PURPLE and card.is_single_block:
                counter["purple double"] += 1
            if card.treat == Treat.PLUMB:
                counter["plumb"] += 1
            if card.treat == Treat.CANDY_CANE:
                counter["candy cane"] += 1
            if card.treat == Treat.GUMDROP:
                counter["gumdrop"] += 1
            if card.treat == Treat.LOLLIPOP:
                counter["lollipop"] += 1
            if card.treat == Treat.NUT:
                counter["nut"] += 1
            if card.treat == Treat.FROST:
                counter["frost"] += 1

        complete_deck_values: Dict[str, int] = {
            "red single": 6,
            "red double": 4,
            "orange single": 6,
            "orange double": 3,
            "yellow single": 6,
            "yellow double": 4,
            "green single": 6,
            "green double": 3,
            "blue single": 6,
            "blue double": 4,
            "purple single": 6,
            "purple double": 4,
            "plumb": 1,
            "candy cane": 1,
            "gumdrop": 1,
            "lollipop": 1,
            "nut": 1,
            "frost": 1,
        }

        for key in counter:
            if counter[key] > complete_deck_values[key]:
                return False

        return True