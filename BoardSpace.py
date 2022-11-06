from enum import Enum

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

class ShortcutSpace(BoardSpace):
    def __init__(self, color: Color, position: int, shortcut: Shortcut) -> None:
        super().__init__(color, position)
        self.shortcut: Shortcut = shortcut

class TreatSpace(BoardSpace):
    def __init__(self, treat: Treat, position: int, color: Color = Color.PINK, sticky: bool = False) -> None:
        super().__init__(color, position, sticky)
        self.treat: Treat = treat