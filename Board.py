from typing import NamedTuple, Union
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
            raise ValueError("position must be in between 0 and 136 inclusive")
        if sticky:
            is_sticky_1: bool = position == 7 and color == Color.YELLOW
            is_sticky_2: bool = position == 13 and color == Color.BLUE
            is_sticky_3: bool = position == 19 and color == Color.RED

            if not is_sticky_1 and not is_sticky_2 and not is_sticky_3:
                raise ValueError("Invalid sticky space")

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
        if treat is Treat.PLUMB:
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

class BoardSpaces(NamedTuple):
    StartSpace: BoardSpace
    RedSpace_0: BoardSpace
    PurpleSpace_0: BoardSpace
    YellowSpace_0: BoardSpace
    BlueSpace_0: BoardSpace
    RainbowTrail: ShortcutSpace
    GreenSpace_0: BoardSpace
    RedSpace_1: BoardSpace
    PurpleSpace_1: BoardSpace
    Plumb: TreatSpace
    YellowSpace_1: BoardSpace
    BlueSpace_1: BoardSpace
    OrangeSpace_1: BoardSpace
    GreenSpace_1: BoardSpace
    RedSpace_2: BoardSpace
    PurpleSpace_2: BoardSpace
    YellowSpace_2: BoardSpace
    BlueSpace_2: BoardSpace
    CandyCane: TreatSpace
    OrangeSpace_2: BoardSpace
    GreenSpace_2: BoardSpace
    RedSpace_3: BoardSpace
    PurpleSpace_3: BoardSpace
    YellowSpace_3: BoardSpace
    BlueSpace_3: BoardSpace
    OrangeSpace_3: BoardSpace
    GreenSpace_3: BoardSpace
    RedSpace_4: BoardSpace
    PurpleSpace_4: BoardSpace
    YellowSpace_4: BoardSpace
    BlueSpace_4: BoardSpace
    OrangeSpace_4: BoardSpace
    GreenSpace_4: BoardSpace
    RedSpace_5: BoardSpace
    GumdropPass: ShortcutSpace
    YellowSpace_5: BoardSpace
    BlueSpace_5: BoardSpace
    OrangeSpace_5: BoardSpace
    GreenSpace_5: BoardSpace
    RedSpace_6: BoardSpace
    PurpleSpace_6: BoardSpace
    YellowSpace_6: BoardSpace
    BlueSpace_6: BoardSpace
    Gumdrop: TreatSpace
    OrangeSpace_6: BoardSpace
    GreenSpace_6: BoardSpace
    RedSpace_7: BoardSpace
    PurpleSpace_7: BoardSpace
    StickySpace_0: BoardSpace
    BlueSpace_7: BoardSpace
    OrangeSpace_7: BoardSpace
    GreenSpace_7: BoardSpace
    RedSpace_8: BoardSpace
    PurpleSpace_8: BoardSpace
    YellowSpace_8: BoardSpace
    BlueSpace_8: BoardSpace
    OrangeSpace_8: BoardSpace
    GreenSpace_8: BoardSpace
    RedSpace_9: BoardSpace
    PurpleSpace_9: BoardSpace
    YellowSpace_9: BoardSpace
    BlueSpace_9: BoardSpace
    OrangeSpace_9: BoardSpace
    GreenSpace_9: BoardSpace
    RedSpace_10: BoardSpace
    PurpleSpace_10: BoardSpace
    YellowSpace_10: BoardSpace
    BlueSpace_10: BoardSpace
    OrangeSpace_10: BoardSpace
    GreenSpace_10: BoardSpace
    RedSpace_11: BoardSpace
    PurpleSpace_11: BoardSpace
    YellowSpace_11: BoardSpace
    BlueSpace_11: BoardSpace
    OrangeSpace_11: BoardSpace
    Nut: TreatSpace
    GreenSpace_11: BoardSpace
    RedSpace_12: BoardSpace
    PurpleSpace_12: BoardSpace
    YellowSpace_12: BoardSpace
    BlueSpace_12: BoardSpace
    OrangeSpace_12: BoardSpace
    GreenSpace_12: BoardSpace
    RedSpace_13: BoardSpace
    PurpleSpace_13: BoardSpace
    YellowSpace_13: BoardSpace
    StickySpace_1: BoardSpace
    OrangeSpace_13: BoardSpace
    GreenSpace_13: BoardSpace
    RedSpace_14: BoardSpace
    PurpleSpace_14: BoardSpace
    YellowSpace_14: BoardSpace
    BlueSpace_14: BoardSpace
    OrangeSpace_14: BoardSpace
    GreenSpace_14: BoardSpace
    RedSpace_15: BoardSpace
    Lollipop: TreatSpace
    PurpleSpace_15: BoardSpace
    YellowSpace_15: BoardSpace
    BlueSpace_15: BoardSpace
    OrangeSpace_15: BoardSpace
    GreenSpace_15: BoardSpace
    RedSpace_16: BoardSpace
    PurpleSpace_16: BoardSpace
    Frost: TreatSpace
    YellowSpace_16: BoardSpace
    BlueSpace_16: BoardSpace
    OrangeSpace_16: BoardSpace
    GreenSpace_16: BoardSpace
    RedSpace_17: BoardSpace
    PurpleSpace_17: BoardSpace
    YellowSpace_17: BoardSpace
    BlueSpace_17: BoardSpace
    OrangeSpace_17: BoardSpace
    GreenSpace_17: BoardSpace
    RedSpace_18: BoardSpace
    PurpleSpace_18: BoardSpace
    YellowSpace_18: BoardSpace
    BlueSpace_18: BoardSpace
    OrangeSpace_18: BoardSpace
    GreenSpace_18: BoardSpace
    StickySpace_2: BoardSpace
    PurpleSpace_19: BoardSpace
    YellowSpace_19: BoardSpace
    BlueSpace_19: BoardSpace
    OrangeSpace_19: BoardSpace
    GreenSpace_19: BoardSpace
    RedSpace_20: BoardSpace
    PurpleSpace_20: BoardSpace
    YellowSpace_20: BoardSpace
    BlueSpace_20: BoardSpace
    OrangeSpace_20: BoardSpace
    GreenSpace_20: BoardSpace
    RedSpace_21: BoardSpace
    PurpleSpace_21: BoardSpace
    EndSpace: BoardSpace

class Board:
    def __init__(self) -> None:
        self.board_spaces: BoardSpaces = self.generate_board()

    def generate_board(self) -> BoardSpaces:
        return BoardSpaces(
            BoardSpace(Color.START, 0),
            BoardSpace(Color.RED, 0),
            BoardSpace(Color.PURPLE, 0),
            BoardSpace(Color.YELLOW, 0),
            BoardSpace(Color.BLUE, 0),
            ShortcutSpace(Shortcut.RAINBOW_TRAIL),
            BoardSpace(Color.GREEN, 0),
            BoardSpace(Color.RED, 1),
            BoardSpace(Color.PURPLE, 1),
            TreatSpace(Treat.PLUMB),
            BoardSpace(Color.YELLOW, 1),
            BoardSpace(Color.BLUE, 1),
            BoardSpace(Color.ORANGE, 1),
            BoardSpace(Color.GREEN, 1),
            BoardSpace(Color.RED, 2),
            BoardSpace(Color.PURPLE, 2),
            BoardSpace(Color.YELLOW, 2),
            BoardSpace(Color.BLUE, 2),
            TreatSpace(Treat.CANDY_CANE),
            BoardSpace(Color.ORANGE, 2),
            BoardSpace(Color.GREEN, 2),
            BoardSpace(Color.RED, 3),
            BoardSpace(Color.PURPLE, 3),
            BoardSpace(Color.YELLOW, 3),
            BoardSpace(Color.BLUE, 3),
            BoardSpace(Color.ORANGE, 3),
            BoardSpace(Color.GREEN, 3),
            BoardSpace(Color.RED, 4),
            BoardSpace(Color.PURPLE, 4),
            BoardSpace(Color.YELLOW, 4),
            BoardSpace(Color.BLUE, 4),
            BoardSpace(Color.ORANGE, 4),
            BoardSpace(Color.GREEN, 4),
            BoardSpace(Color.RED, 5),
            ShortcutSpace(Shortcut.GUMDROP_PASS),
            BoardSpace(Color.YELLOW, 5),
            BoardSpace(Color.BLUE, 5),
            BoardSpace(Color.ORANGE, 5),
            BoardSpace(Color.GREEN, 5),
            BoardSpace(Color.RED, 6),
            BoardSpace(Color.PURPLE, 6),
            BoardSpace(Color.YELLOW, 6),
            BoardSpace(Color.BLUE, 6),
            TreatSpace(Treat.GUMDROP),
            BoardSpace(Color.ORANGE, 6),
            BoardSpace(Color.GREEN, 6),
            BoardSpace(Color.RED, 7),
            BoardSpace(Color.PURPLE, 7),
            BoardSpace(Color.YELLOW, 7, sticky=True),
            BoardSpace(Color.BLUE, 7),
            BoardSpace(Color.ORANGE, 7),
            BoardSpace(Color.GREEN, 7),
            BoardSpace(Color.RED, 8),
            BoardSpace(Color.PURPLE, 8),
            BoardSpace(Color.YELLOW, 8),
            BoardSpace(Color.BLUE, 8),
            BoardSpace(Color.ORANGE, 8),
            BoardSpace(Color.GREEN, 8),
            BoardSpace(Color.RED, 9),
            BoardSpace(Color.PURPLE, 9),
            BoardSpace(Color.YELLOW, 9),
            BoardSpace(Color.BLUE, 9),
            BoardSpace(Color.ORANGE, 9),
            BoardSpace(Color.GREEN, 9),
            BoardSpace(Color.RED, 10),
            BoardSpace(Color.PURPLE, 10),
            BoardSpace(Color.YELLOW, 10),
            BoardSpace(Color.BLUE, 10),
            BoardSpace(Color.ORANGE, 10),
            BoardSpace(Color.GREEN, 10),
            BoardSpace(Color.RED, 11),
            BoardSpace(Color.PURPLE, 11),
            BoardSpace(Color.YELLOW, 11),
            BoardSpace(Color.BLUE, 11),
            BoardSpace(Color.ORANGE, 11),
            TreatSpace(Treat.NUT),
            BoardSpace(Color.GREEN, 11),
            BoardSpace(Color.RED, 12),
            BoardSpace(Color.PURPLE, 12),
            BoardSpace(Color.YELLOW, 12),
            BoardSpace(Color.BLUE, 12),
            BoardSpace(Color.ORANGE, 12),
            BoardSpace(Color.GREEN, 12),
            BoardSpace(Color.RED, 13),
            BoardSpace(Color.PURPLE, 13),
            BoardSpace(Color.YELLOW, 13),
            BoardSpace(Color.BLUE, 13, sticky=True),
            BoardSpace(Color.ORANGE, 13),
            BoardSpace(Color.GREEN, 13),
            BoardSpace(Color.RED, 14),
            BoardSpace(Color.PURPLE, 14),
            BoardSpace(Color.YELLOW, 14),
            BoardSpace(Color.BLUE, 14),
            BoardSpace(Color.ORANGE, 14),
            BoardSpace(Color.GREEN, 14),
            BoardSpace(Color.RED, 15),
            TreatSpace(Treat.LOLLIPOP),
            BoardSpace(Color.PURPLE, 15),
            BoardSpace(Color.YELLOW, 15),
            BoardSpace(Color.BLUE, 15),
            BoardSpace(Color.ORANGE, 15),
            BoardSpace(Color.GREEN, 15),
            BoardSpace(Color.RED, 16),
            BoardSpace(Color.PURPLE, 16),
            TreatSpace(Treat.FROST),
            BoardSpace(Color.YELLOW, 16),
            BoardSpace(Color.BLUE, 16),
            BoardSpace(Color.ORANGE, 16),
            BoardSpace(Color.GREEN, 16),
            BoardSpace(Color.RED, 17),
            BoardSpace(Color.PURPLE, 17),
            BoardSpace(Color.YELLOW, 17),
            BoardSpace(Color.BLUE, 17),
            BoardSpace(Color.ORANGE, 17),
            BoardSpace(Color.GREEN, 17),
            BoardSpace(Color.RED, 18),
            BoardSpace(Color.PURPLE, 18),
            BoardSpace(Color.YELLOW, 18),
            BoardSpace(Color.BLUE, 18),
            BoardSpace(Color.ORANGE, 18),
            BoardSpace(Color.GREEN, 18),
            BoardSpace(Color.RED, 19, sticky=True),
            BoardSpace(Color.PURPLE, 19),
            BoardSpace(Color.YELLOW, 19),
            BoardSpace(Color.BLUE, 19),
            BoardSpace(Color.ORANGE, 19),
            BoardSpace(Color.GREEN, 19),
            BoardSpace(Color.RED, 20),
            BoardSpace(Color.PURPLE, 20),
            BoardSpace(Color.YELLOW, 20),
            BoardSpace(Color.BLUE, 20),
            BoardSpace(Color.ORANGE, 20),
            BoardSpace(Color.GREEN, 20),
            BoardSpace(Color.RED, 21),
            BoardSpace(Color.PURPLE, 21),
            BoardSpace(Color.END, 0),
        )