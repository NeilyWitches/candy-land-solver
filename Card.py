from BoardSpace import (Color, Treat)

class Card:
    def __init__(self, color: Color, is_single_block: bool = True) -> None:
        self.is_single_block: bool = is_single_block
        self.color: Color = color

class TreatCard(Card):
    def __init__(self, treat: Treat, is_single_block: bool = True) -> None:
        super().__init__(is_single_block)
        self.color: Color = Color.PINK
        self.treat: Treat = treat;