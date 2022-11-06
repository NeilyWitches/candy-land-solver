from enum import Enum

class Color(Enum):
    RED = 1
    PURPLE = 2
    YELLOW = 3
    BLUE = 4
    ORANGE = 5
    GREEN = 6
    PINK = 7

class Treat(Enum):
    CHOCOLATE = 1
    ICE_CREAM = 2
    LOLLI_POP = 3
    GUM_DROP = 4
    PEPPERMINT = 5

class Card:
    def __init__(self, is_single_block: bool, color: Color) -> None:
        self.is_single_block = is_single_block
        self.color = color

class TreatCard(Card):
    def __init__(self, is_single_block: bool, color: Color) -> None:
        super().__init__(is_single_block, color)
        self.treat = Treat