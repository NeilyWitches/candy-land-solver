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
        if color is Color.START and position != 0:
            raise ValueError("Cannot create a starting board space with a position other than 0")
        if color is Color.END and position != 136:
            raise ValueError("Cannot create an ending board space with a position other than 136")
        if color is Color.PINK:
            raise ValueError(
                """PINK is reserved for TreatSpaces, if you are trying to make a treat space object, 
                do not pass a color into BoardSpace(), pass in a treat instead into TreatSpace, e.g: 
                TreatSpace(Treat.CANDY_CANE, 15)""")
        if position < 0 or position > 136:
            raise ValueError("position must be in between 0 and 136 inclusive")
            
        self.color: Color = color
        self.position: int = position
        self.sticky: bool = sticky
        self.shortcut: Union[None, Shortcut] = None
        self.treat: Union[None, Treat] = None

class ShortcutSpace(BoardSpace):
    def __init__(self, shortcut: Shortcut) -> None:
        self.shortcut = shortcut
        self.position: int
        if shortcut is Shortcut.RAINBOW_TRAIL:
            self.color = Color.ORANGE
            self.position = 5
        elif shortcut is Shortcut.GUMDROP_PASS:
            self.color = Color.PURPLE
            self.position = 34
        else:
            raise ValueError("Invalid shortcut")
        self.sticky = False
        self.treat = None

class TreatSpace(BoardSpace):
    def __init__(self, treat: Treat) -> None:
        self.treat = treat
        if treat is Treat.PLUMB:
            self.position = 9
        elif treat is Treat.CANDY_CANE:
            self.position = 18
        elif treat is Treat.GUMDROP:
            self.position = 43
        elif treat is Treat.NUT:
            self.position = 75
        elif treat is Treat.LOLLIPOP:
            self.position = 96
        elif treat is Treat.FROST:
            self.position = 104
        else:
            raise ValueError("Invalid treat")
        self.color = Color.PINK
        self.sticky = False
        self.shortcut = None