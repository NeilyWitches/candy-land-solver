from enum import Enum
from typing import Union

class Shortcut(Enum):
    RAINBOW_TRAIL = 1
    GUMDROP_PASS = 2

class Color(Enum):
    START = 1
    RED = 2
    PURPLE = 3
    YELLOW = 4
    BLUE = 5
    ORANGE = 6
    GREEN = 7
    PINK = 8
    END = 9

class Treat(Enum):
    PLUMB = 1
    CANDY_CANE = 2
    GUMDROP = 3
    LOLLIPOP = 4
    NUT = 5
    FROST = 6
    
class BoardSpace:
    def __init__(self, color: Color, position: int, sticky: bool = False) -> None:
        self.color: Color = color
        self.position: int = position
        self.sticky: bool = sticky
        self.shortcut: Union[None, Shortcut] = None
        self.treat: Union[None, Treat] = None

class ShortcutSpace(BoardSpace):
    def __init__(self, color: Color, position: int, shortcut: Shortcut) -> None:
        self.color = color
        self.position = position
        self.sticky = False
        self.shortcut = shortcut
        self.treat = None

class TreatSpace(BoardSpace):
    def __init__(self, treat: Treat, position: int) -> None:
        self.color = Color.PINK
        self.position = position
        self.sticky = False
        self.shortcut = None
        self.treat: Treat = treat