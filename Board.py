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
        if color is Color.END and position != BoardSpaces.length() - 1:
            raise ValueError(
                f"Cannot create an ending board space with a position other than {BoardSpaces.length() - 1}")
        if color is Color.PINK:
            raise ValueError(
                """PINK is reserved for TreatSpaces, if you are trying to make a treat space object, 
                do not pass a color into BoardSpace(), pass in a treat instead into TreatSpace, e.g: 
                TreatSpace(Treat.CANDY_CANE, 15)"""
            )
        if position < 0 or position > BoardSpaces.length():
            raise ValueError("position must be in between 0 and 136 inclusive")
        if sticky:
            is_sticky_1: bool = position == 48 and color == Color.YELLOW
            is_sticky_2: bool = position == 86 and color == Color.BLUE
            is_sticky_3: bool = position == 122 and color == Color.RED

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

class BoardSpaces(NamedTuple):
    StartSpace: BoardSpace
    BoardSpace_1: BoardSpace
    BoardSpace_2: BoardSpace
    BoardSpace_3: BoardSpace
    BoardSpace_4: BoardSpace
    RainbowTrail: ShortcutSpace
    BoardSpace_6: BoardSpace
    BoardSpace_7: BoardSpace
    BoardSpace_8: BoardSpace
    Plum: TreatSpace
    BoardSpace_10: BoardSpace
    BoardSpace_11: BoardSpace
    BoardSpace_12: BoardSpace
    BoardSpace_13: BoardSpace
    BoardSpace_14: BoardSpace
    BoardSpace_15: BoardSpace
    BoardSpace_16: BoardSpace
    BoardSpace_17: BoardSpace
    CandyCane: TreatSpace
    BoardSpace_19: BoardSpace
    BoardSpace_20: BoardSpace
    BoardSpace_21: BoardSpace
    BoardSpace_22: BoardSpace
    BoardSpace_23: BoardSpace
    BoardSpace_24: BoardSpace
    BoardSpace_25: BoardSpace
    BoardSpace_26: BoardSpace
    BoardSpace_27: BoardSpace
    BoardSpace_28: BoardSpace
    BoardSpace_29: BoardSpace
    BoardSpace_30: BoardSpace
    BoardSpace_31: BoardSpace
    BoardSpace_32: BoardSpace
    BoardSpace_33: BoardSpace
    GumdropPass: ShortcutSpace
    BoardSpace_35: BoardSpace
    BoardSpace_36: BoardSpace
    BoardSpace_37: BoardSpace
    BoardSpace_38: BoardSpace
    BoardSpace_39: BoardSpace
    BoardSpace_40: BoardSpace
    BoardSpace_41: BoardSpace
    BoardSpace_42: BoardSpace
    GumDrop: TreatSpace
    BoardSpace_44: BoardSpace
    BoardSpace_45: BoardSpace
    BoardSpace_46: BoardSpace
    BoardSpace_47: BoardSpace
    StickySpace_1: BoardSpace
    BoardSpace_49: BoardSpace
    BoardSpace_50: BoardSpace
    BoardSpace_51: BoardSpace
    BoardSpace_52: BoardSpace
    BoardSpace_53: BoardSpace
    BoardSpace_54: BoardSpace
    BoardSpace_55: BoardSpace
    BoardSpace_56: BoardSpace
    BoardSpace_57: BoardSpace
    BoardSpace_58: BoardSpace
    BoardSpace_59: BoardSpace
    BoardSpace_60: BoardSpace
    BoardSpace_61: BoardSpace
    BoardSpace_62: BoardSpace
    BoardSpace_63: BoardSpace
    BoardSpace_64: BoardSpace
    BoardSpace_65: BoardSpace
    BoardSpace_66: BoardSpace
    BoardSpace_67: BoardSpace
    BoardSpace_68: BoardSpace
    BoardSpace_69: BoardSpace
    BoardSpace_70: BoardSpace
    BoardSpace_71: BoardSpace
    BoardSpace_72: BoardSpace
    BoardSpace_73: BoardSpace
    BoardSpace_74: BoardSpace
    Nut: TreatSpace
    BoardSpace_76: BoardSpace
    BoardSpace_77: BoardSpace
    BoardSpace_78: BoardSpace
    BoardSpace_79: BoardSpace
    BoardSpace_80: BoardSpace
    BoardSpace_81: BoardSpace
    BoardSpace_82: BoardSpace
    BoardSpace_83: BoardSpace
    BoardSpace_84: BoardSpace
    BoardSpace_85: BoardSpace
    StickySpace_2: BoardSpace
    BoardSpace_87: BoardSpace
    BoardSpace_88: BoardSpace
    BoardSpace_89: BoardSpace
    BoardSpace_90: BoardSpace
    BoardSpace_91: BoardSpace
    BoardSpace_92: BoardSpace
    BoardSpace_93: BoardSpace
    BoardSpace_94: BoardSpace
    BoardSpace_95: BoardSpace
    LolliPop: TreatSpace
    BoardSpace_97: BoardSpace
    BoardSpace_98: BoardSpace
    BoardSpace_99: BoardSpace
    BoardSpace_100: BoardSpace
    BoardSpace_101: BoardSpace
    BoardSpace_102: BoardSpace
    BoardSpace_103: BoardSpace
    Frost: TreatSpace
    BoardSpace_105: BoardSpace
    BoardSpace_106: BoardSpace
    BoardSpace_107: BoardSpace
    BoardSpace_108: BoardSpace
    BoardSpace_109: BoardSpace
    BoardSpace_110: BoardSpace
    BoardSpace_111: BoardSpace
    BoardSpace_112: BoardSpace
    BoardSpace_113: BoardSpace
    BoardSpace_114: BoardSpace
    BoardSpace_115: BoardSpace
    BoardSpace_116: BoardSpace
    BoardSpace_117: BoardSpace
    BoardSpace_118: BoardSpace
    BoardSpace_119: BoardSpace
    BoardSpace_120: BoardSpace
    BoardSpace_121: BoardSpace
    StickySpace_3: BoardSpace
    BoardSpace_123: BoardSpace
    BoardSpace_124: BoardSpace
    BoardSpace_125: BoardSpace
    BoardSpace_126: BoardSpace
    BoardSpace_127: BoardSpace
    BoardSpace_128: BoardSpace
    BoardSpace_129: BoardSpace
    BoardSpace_130: BoardSpace
    BoardSpace_131: BoardSpace
    BoardSpace_132: BoardSpace
    BoardSpace_133: BoardSpace
    BoardSpace_134: BoardSpace
    BoardSpace_135: BoardSpace
    EndSpace: BoardSpace

    @classmethod
    def length(cls):
        return len([key for key in cls.__dict__.keys() if key[0] != '_']) - 1

class Board:
    def __init__(self) -> None:
        self.board_spaces: BoardSpaces = self.generate_board()

    def generate_board(self) -> BoardSpaces:
        board: BoardSpaces = BoardSpaces(
            BoardSpace(Color.START, 0),
            BoardSpace(Color.RED, 1),
            BoardSpace(Color.PURPLE, 2),
            BoardSpace(Color.YELLOW, 3),
            BoardSpace(Color.BLUE, 4),
            ShortcutSpace(Shortcut.RAINBOW_TRAIL),
            BoardSpace(Color.GREEN, 6),
            BoardSpace(Color.RED, 7),
            BoardSpace(Color.PURPLE, 8),
            TreatSpace(Treat.PLUMB),
            BoardSpace(Color.YELLOW, 10),
            BoardSpace(Color.BLUE, 11),
            BoardSpace(Color.ORANGE, 12),
            BoardSpace(Color.GREEN, 13),
            BoardSpace(Color.RED, 14),
            BoardSpace(Color.PURPLE, 15),
            BoardSpace(Color.YELLOW, 16),
            BoardSpace(Color.BLUE, 17),
            TreatSpace(Treat.CANDY_CANE),
            BoardSpace(Color.ORANGE, 19),
            BoardSpace(Color.GREEN, 20),
            BoardSpace(Color.RED, 21),
            BoardSpace(Color.PURPLE, 22),
            BoardSpace(Color.YELLOW, 23),
            BoardSpace(Color.BLUE, 24),
            BoardSpace(Color.ORANGE, 25),
            BoardSpace(Color.GREEN, 26),
            BoardSpace(Color.RED, 27),
            BoardSpace(Color.PURPLE, 28),
            BoardSpace(Color.YELLOW, 29),
            BoardSpace(Color.BLUE, 30),
            BoardSpace(Color.ORANGE, 31),
            BoardSpace(Color.GREEN, 32),
            BoardSpace(Color.RED, 33),
            ShortcutSpace(Shortcut.GUMDROP_PASS),
            BoardSpace(Color.YELLOW, 35),
            BoardSpace(Color.BLUE, 36),
            BoardSpace(Color.ORANGE, 37),
            BoardSpace(Color.GREEN, 38),
            BoardSpace(Color.RED, 39),
            BoardSpace(Color.PURPLE, 40),
            BoardSpace(Color.YELLOW, 41),
            BoardSpace(Color.BLUE, 42),
            TreatSpace(Treat.GUMDROP),
            BoardSpace(Color.ORANGE, 44),
            BoardSpace(Color.GREEN, 45),
            BoardSpace(Color.RED, 46),
            BoardSpace(Color.PURPLE, 47),
            BoardSpace(Color.YELLOW, 48, sticky=True),
            BoardSpace(Color.BLUE, 49),
            BoardSpace(Color.ORANGE, 50),
            BoardSpace(Color.GREEN, 51),
            BoardSpace(Color.RED, 52),
            BoardSpace(Color.PURPLE, 53),
            BoardSpace(Color.YELLOW, 54),
            BoardSpace(Color.BLUE, 55),
            BoardSpace(Color.ORANGE, 56),
            BoardSpace(Color.GREEN, 57),
            BoardSpace(Color.RED, 58),
            BoardSpace(Color.PURPLE, 59),
            BoardSpace(Color.YELLOW, 60),
            BoardSpace(Color.BLUE, 61),
            BoardSpace(Color.ORANGE, 62),
            BoardSpace(Color.GREEN, 63),
            BoardSpace(Color.RED, 64),
            BoardSpace(Color.PURPLE, 65),
            BoardSpace(Color.YELLOW, 66),
            BoardSpace(Color.BLUE, 67),
            BoardSpace(Color.ORANGE, 68),
            BoardSpace(Color.GREEN, 69),
            BoardSpace(Color.RED, 70),
            BoardSpace(Color.PURPLE, 71),
            BoardSpace(Color.YELLOW, 72),
            BoardSpace(Color.BLUE, 73),
            BoardSpace(Color.ORANGE, 74),
            TreatSpace(Treat.NUT),
            BoardSpace(Color.GREEN, 76),
            BoardSpace(Color.RED, 77),
            BoardSpace(Color.PURPLE, 78),
            BoardSpace(Color.YELLOW, 79),
            BoardSpace(Color.BLUE, 80),
            BoardSpace(Color.ORANGE, 81),
            BoardSpace(Color.GREEN, 82),
            BoardSpace(Color.RED, 83),
            BoardSpace(Color.PURPLE, 84),
            BoardSpace(Color.YELLOW, 85),
            BoardSpace(Color.BLUE, 86, sticky=True),
            BoardSpace(Color.ORANGE, 87),
            BoardSpace(Color.GREEN, 88),
            BoardSpace(Color.RED, 89),
            BoardSpace(Color.PURPLE, 90),
            BoardSpace(Color.YELLOW, 91),
            BoardSpace(Color.BLUE, 92),
            BoardSpace(Color.ORANGE, 93),
            BoardSpace(Color.GREEN, 94),
            BoardSpace(Color.RED, 95),
            TreatSpace(Treat.LOLLIPOP),
            BoardSpace(Color.PURPLE, 97),
            BoardSpace(Color.YELLOW, 98),
            BoardSpace(Color.BLUE, 99),
            BoardSpace(Color.ORANGE, 100),
            BoardSpace(Color.GREEN, 101),
            BoardSpace(Color.RED, 102),
            BoardSpace(Color.PURPLE, 103),
            TreatSpace(Treat.FROST),
            BoardSpace(Color.YELLOW, 105),
            BoardSpace(Color.BLUE, 106),
            BoardSpace(Color.ORANGE, 107),
            BoardSpace(Color.GREEN, 108),
            BoardSpace(Color.RED, 109),
            BoardSpace(Color.PURPLE, 110),
            BoardSpace(Color.RED, 111),
            BoardSpace(Color.YELLOW, 112),
            BoardSpace(Color.BLUE, 113),
            BoardSpace(Color.ORANGE, 114),
            BoardSpace(Color.GREEN, 115),
            BoardSpace(Color.RED, 116),
            BoardSpace(Color.PURPLE, 117),
            BoardSpace(Color.YELLOW, 118),
            BoardSpace(Color.BLUE, 119),
            BoardSpace(Color.ORANGE, 120),
            BoardSpace(Color.GREEN, 121),
            BoardSpace(Color.RED, 122, sticky=True),
            BoardSpace(Color.PURPLE, 123),
            BoardSpace(Color.YELLOW, 124),
            BoardSpace(Color.BLUE, 125),
            BoardSpace(Color.ORANGE, 126),
            BoardSpace(Color.GREEN, 127),
            BoardSpace(Color.RED, 128),
            BoardSpace(Color.PURPLE, 129),
            BoardSpace(Color.YELLOW, 130),
            BoardSpace(Color.BLUE, 131),
            BoardSpace(Color.ORANGE, 132),
            BoardSpace(Color.GREEN, 133),
            BoardSpace(Color.RED, 134),
            BoardSpace(Color.PURPLE, 135),
            BoardSpace(Color.END, 136),
        )
        
        return board