from board_space import Color, Treat
from typing import Union

class Card:
    def __init__(self, color: Color, is_single_block: bool = True) -> None:
        self.is_single_block: bool = is_single_block
        self.color: Color = color
        self.treat: Union[None, Treat] = None

class TreatCard(Card):
    def __init__(self, treat: Treat) -> None:
        self.is_single_block = True
        self.color = Color.PINK
        self.treat = treat