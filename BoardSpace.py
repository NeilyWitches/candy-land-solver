from Card import ( Color, Treat )
from enum import Enum

class Shortcut(Enum):
    PEPPERMINT_PASS = 1
    GUMMY_PASS = 2

class BoardSpace:
    def __init__(self, color: Color, has_x: bool=False) -> None:
        self.color = color
        self.has_x = has_x

class ShortcutSpace(BoardSpace):
    def __init__(self, color: Color, shortcut: Shortcut) -> None:
        super().__init__(color)
        self.shortcut = shortcut

class TreatSpace(BoardSpace):
    def __init__(self, treat: Treat) -> None:
        self.color = Color.PINK
        self.treat = treat    