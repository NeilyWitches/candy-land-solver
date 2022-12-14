from typing import Set
from card import *
from discard_pile import DiscardPile
from board import *

class Deck:
    def __init__(self) -> None:
        self.cards: Set[Card] = self.generate_deck()

    def generate_deck(self) -> Set[Card]:
        cards: Set[Card] = set()

        def make_several_cards(is_single_block: bool, color: Color, quantity: int) -> None:
            for _ in range(quantity):
                cards.add(Card(color, is_single_block))
            
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

        cards.add(TreatCard(Treat.PLUM))
        cards.add(TreatCard(Treat.CANDY_CANE))
        cards.add(TreatCard(Treat.GUMDROP))
        cards.add(TreatCard(Treat.LOLLIPOP))
        cards.add(TreatCard(Treat.NUT))
        cards.add(TreatCard(Treat.FROST))

        return cards

    def draw_card(self, card: Card) -> None:
        self.cards.remove(card)
        
        if len(self.cards) == 0:
            self.cards = self.generate_deck()

    def find_card(self, user_input: str) -> Card:
        inputted_card: Card

        if user_input not in {"r", "rr", "p", "pp", "y", "yy", "b", "bb", 
        "o", "oo", "g", "gg", "plum", "candy_cane", "gumdrop", "lollipop", 
        "nut", "frost"}:
            raise ValueError("Invalid input")

        

        color: Color = Color.PINK
        is_single_block: bool = True
        treat: Union[None, Treat] = None
        if len(user_input) <= 2:
            if user_input[0] == "r":
                color = Color.RED
            if user_input[0] == "p":
                color = Color.PURPLE
            if user_input[0] == "y":
                color = Color.YELLOW
            if user_input[0] == "b":
                color = Color.BLUE
            if user_input[0] == "o":
                color = Color.ORANGE
            if user_input[0] == "g":
                color = Color.GREEN
        if len(user_input) == 2:
            is_single_block = False
        if len(user_input) > 2:
            treat = Treat[user_input.upper()]

        card_not_found = True
        for card in self.cards:
            if card.color == color and card.is_single_block == is_single_block and card.treat == treat:
                inputted_card = card
                card_not_found = False

        if card_not_found:
            raise ValueError("Ran out of that card! May need to modify deck.")

        return inputted_card

    def copy(self) -> 'Deck':
        copy: Deck = Deck()
        copy.cards = set()
        for card in self.cards:
            if card.treat is not None:
                copy.cards.add(TreatCard(card.treat))
            else:
                copy.cards.add(Card(card.color, card.is_single_block))

        return copy