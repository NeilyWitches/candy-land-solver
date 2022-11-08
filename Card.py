from board_space import Color, Treat
from typing import Union

class Card:
    def __init__(self, color: Color, is_single_block: bool = True) -> None:
        if color is Color.START or color is Color.PINK or color is Color.END:
            raise ValueError("A card cannot be that color")
        self.is_single_block: bool = is_single_block
        self.color: Color = color
        self.treat: Union[None, Treat] = None

class TreatCard(Card):
    def __init__(self, treat: Treat) -> None:
        self.is_single_block = True
        self.color = Color.PINK
        self.treat = treat