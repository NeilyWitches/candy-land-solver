from typing import List
from BoardSpace import (BoardSpace, ShortcutSpace, Shortcut, TreatSpace, Color, Treat)

class Board:
    def __init__(self) -> None:
        self.board: List[BoardSpace] = self.generate_board()

    def generate_board(self) -> List[BoardSpace]:
        board: List[BoardSpace] = [BoardSpace(Color.START, 0)]
        board.append(BoardSpace(Color.RED, 1))
        board.append(BoardSpace(Color.PURPLE, 2))
        board.append(BoardSpace(Color.YELLOW, 3))
        board.append(BoardSpace(Color.BLUE, 4))
        board.append(ShortcutSpace(Color.ORANGE, 5, Shortcut.RAINBOW_TRAIL))
        board.append(BoardSpace(Color.GREEN, 6))
        board.append(BoardSpace(Color.RED, 7))
        board.append(BoardSpace(Color.PURPLE, 8))
        board.append(TreatSpace(Treat.PLUMB, 9))
        board.append(BoardSpace(Color.YELLOW, 10))
        board.append(BoardSpace(Color.BLUE, 11))
        board.append(BoardSpace(Color.ORANGE, 12))
        board.append(BoardSpace(Color.GREEN, 13))
        board.append(BoardSpace(Color.RED, 14))
        board.append(BoardSpace(Color.PURPLE, 15))
        board.append(BoardSpace(Color.YELLOW, 16))
        board.append(BoardSpace(Color.BLUE, 17))
        board.append(TreatSpace(Treat.CANDY_CANE, 18))
        board.append(BoardSpace(Color.ORANGE, 19))
        board.append(BoardSpace(Color.GREEN, 20))
        board.append(BoardSpace(Color.RED, 21))
        board.append(BoardSpace(Color.PURPLE, 22))
        board.append(BoardSpace(Color.YELLOW, 23))
        board.append(BoardSpace(Color.BLUE, 24))
        board.append(BoardSpace(Color.ORANGE, 25))
        board.append(BoardSpace(Color.GREEN, 26))
        board.append(BoardSpace(Color.RED, 27))
        board.append(BoardSpace(Color.PURPLE, 28))
        board.append(BoardSpace(Color.YELLOW, 29))
        board.append(BoardSpace(Color.BLUE, 30))
        board.append(BoardSpace(Color.ORANGE, 31))
        board.append(BoardSpace(Color.GREEN, 32))
        board.append(BoardSpace(Color.RED, 33))
        board.append(ShortcutSpace(Color.PURPLE, 34, Shortcut.GUMDROP_PASS))
        board.append(BoardSpace(Color.YELLOW, 35))
        board.append(BoardSpace(Color.BLUE, 36))
        board.append(BoardSpace(Color.ORANGE, 37))
        board.append(BoardSpace(Color.GREEN, 38))
        board.append(BoardSpace(Color.RED, 39))
        board.append(BoardSpace(Color.PURPLE, 40))
        board.append(BoardSpace(Color.YELLOW, 41))
        board.append(BoardSpace(Color.BLUE, 42))
        board.append(TreatSpace(Treat.GUMDROP, 43))
        board.append(BoardSpace(Color.ORANGE, 44))
        board.append(BoardSpace(Color.GREEN, 45))
        board.append(BoardSpace(Color.RED, 46))
        board.append(BoardSpace(Color.PURPLE, 47))
        board.append(BoardSpace(Color.YELLOW, 48, sticky = True))
        board.append(BoardSpace(Color.BLUE, 49))
        board.append(BoardSpace(Color.ORANGE, 50))
        board.append(BoardSpace(Color.GREEN, 51))
        board.append(BoardSpace(Color.RED, 52))
        board.append(BoardSpace(Color.PURPLE, 53))
        board.append(BoardSpace(Color.YELLOW, 54))
        board.append(BoardSpace(Color.BLUE, 55))
        board.append(BoardSpace(Color.ORANGE, 56))
        board.append(BoardSpace(Color.GREEN, 57))
        board.append(BoardSpace(Color.RED, 58))
        board.append(BoardSpace(Color.PURPLE, 59))
        board.append(BoardSpace(Color.YELLOW, 60))
        board.append(BoardSpace(Color.BLUE, 61))
        board.append(BoardSpace(Color.ORANGE, 62))
        board.append(BoardSpace(Color.GREEN, 63))
        board.append(BoardSpace(Color.RED, 64))
        board.append(BoardSpace(Color.PURPLE, 65))
        board.append(BoardSpace(Color.YELLOW, 66))
        board.append(BoardSpace(Color.BLUE, 67))
        board.append(BoardSpace(Color.ORANGE, 68))
        board.append(BoardSpace(Color.GREEN, 69))
        board.append(BoardSpace(Color.RED, 70))
        board.append(BoardSpace(Color.PURPLE, 71))
        board.append(BoardSpace(Color.YELLOW, 72))
        board.append(BoardSpace(Color.BLUE, 73))
        board.append(BoardSpace(Color.ORANGE, 74))
        board.append(TreatSpace(Treat.NUT, 75))
        board.append(BoardSpace(Color.GREEN, 76))
        board.append(BoardSpace(Color.RED, 77))
        board.append(BoardSpace(Color.PURPLE, 78))
        board.append(BoardSpace(Color.YELLOW, 79))
        board.append(BoardSpace(Color.BLUE, 80))
        board.append(BoardSpace(Color.ORANGE, 81))
        board.append(BoardSpace(Color.GREEN, 82))
        board.append(BoardSpace(Color.RED, 83))
        board.append(BoardSpace(Color.PURPLE, 84))
        board.append(BoardSpace(Color.YELLOW, 85))
        board.append(BoardSpace(Color.BLUE, 86, sticky = True))
        board.append(BoardSpace(Color.ORANGE, 87))
        board.append(BoardSpace(Color.GREEN, 88))
        board.append(BoardSpace(Color.RED, 89))
        board.append(BoardSpace(Color.PURPLE, 90))
        board.append(BoardSpace(Color.YELLOW, 91))
        board.append(BoardSpace(Color.BLUE, 92))
        board.append(BoardSpace(Color.ORANGE, 93))
        board.append(BoardSpace(Color.GREEN, 94))
        board.append(BoardSpace(Color.RED, 95))
        board.append(TreatSpace(Treat.LOLLIPOP, 96))
        board.append(BoardSpace(Color.PURPLE, 97))
        board.append(BoardSpace(Color.YELLOW, 98))
        board.append(BoardSpace(Color.BLUE, 99))
        board.append(BoardSpace(Color.ORANGE, 100))
        board.append(BoardSpace(Color.GREEN, 101))
        board.append(BoardSpace(Color.RED, 102))
        board.append(BoardSpace(Color.PURPLE, 103))
        board.append(TreatSpace(Treat.FROST, 104))
        board.append(BoardSpace(Color.YELLOW, 105))
        board.append(BoardSpace(Color.BLUE, 106))
        board.append(BoardSpace(Color.ORANGE, 107))
        board.append(BoardSpace(Color.GREEN, 108))
        board.append(BoardSpace(Color.RED, 109))
        board.append(BoardSpace(Color.PURPLE, 110))
        board.append(BoardSpace(Color.RED, 111))
        board.append(BoardSpace(Color.YELLOW, 112))
        board.append(BoardSpace(Color.BLUE, 113))
        board.append(BoardSpace(Color.ORANGE, 114))
        board.append(BoardSpace(Color.GREEN, 115))
        board.append(BoardSpace(Color.RED, 116))
        board.append(BoardSpace(Color.PURPLE, 117))
        board.append(BoardSpace(Color.YELLOW, 118))
        board.append(BoardSpace(Color.BLUE, 119))
        board.append(BoardSpace(Color.ORANGE, 120))
        board.append(BoardSpace(Color.GREEN, 121))
        board.append(BoardSpace(Color.RED, 122, sticky = True))
        board.append(BoardSpace(Color.PURPLE, 123))
        board.append(BoardSpace(Color.YELLOW, 124))
        board.append(BoardSpace(Color.BLUE, 125))
        board.append(BoardSpace(Color.ORANGE, 126))
        board.append(BoardSpace(Color.GREEN, 127))
        board.append(BoardSpace(Color.RED, 128))
        board.append(BoardSpace(Color.PURPLE, 129))
        board.append(BoardSpace(Color.YELLOW, 130))
        board.append(BoardSpace(Color.BLUE, 131))
        board.append(BoardSpace(Color.ORANGE, 132))
        board.append(BoardSpace(Color.GREEN, 133))
        board.append(BoardSpace(Color.RED, 134))
        board.append(BoardSpace(Color.PURPLE, 135))
        board.append(BoardSpace(Color.END, 136))
        print(board)
        return board