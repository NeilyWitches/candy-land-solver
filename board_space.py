from typing import Union
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
    PLUM = 1
    CANDY_CANE = 2
    GUMDROP = 3
    LOLLIPOP = 4
    NUT = 5
    FROST = 6


class BoardSpace:
    def __init__(self, color: Color, position: int, sticky: bool = False) -> None:
        if color is Color.START and position != 0:
            raise ValueError(
                "Cannot create a starting board space with a position other than 0")
        if color is Color.END and position != 0:
            raise ValueError(
                f"Cannot create an ending board space with a position other than 0")
        if color is Color.PINK:
            raise ValueError(
                """PINK is reserved for TreatSpaces, if you are trying to make a treat space object, 
                do not pass a color into BoardSpace(), pass in a treat instead into TreatSpace, e.g: 
                TreatSpace(Treat.CANDY_CANE, 15)"""
            )
        if position < 0 or position > 21:
            raise ValueError("position must be in between 0 and 21 inclusive")
        if sticky:
            is_sticky_1: bool = position == 7 and color == Color.YELLOW
            is_sticky_2: bool = position == 13 and color == Color.BLUE
            is_sticky_3: bool = position == 19 and color == Color.RED

            if not is_sticky_1 and not is_sticky_2 and not is_sticky_3:
                raise ValueError("Invalid sticky space")

        if color == Color.ORANGE and position == 0:
            raise ValueError("The space with color Orange and position 0 is reserved for the rainbow trail shortcut")
        if color == Color.PURPLE and position == 5:
            raise ValueError("The space with color Purple and position 5 is reserved for the gumdrop pass shortcut")

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
            self.position = 0
        elif shortcut is Shortcut.GUMDROP_PASS:
            self.color = Color.PURPLE
            self.position = 5
        else:
            raise ValueError("Invalid shortcut")
        self.sticky = False
        self.treat = None


class TreatSpace(BoardSpace):
    def __init__(self, treat: Treat) -> None:
        self.treat = treat
        if treat is Treat.PLUM:
            self.position = 0
        elif treat is Treat.CANDY_CANE:
            self.position = 1
        elif treat is Treat.GUMDROP:
            self.position = 2
        elif treat is Treat.NUT:
            self.position = 3
        elif treat is Treat.LOLLIPOP:
            self.position = 4
        elif treat is Treat.FROST:
            self.position = 5
        else:
            raise ValueError("Invalid treat")
        self.color = Color.PINK
        self.sticky = False
        self.shortcut = None