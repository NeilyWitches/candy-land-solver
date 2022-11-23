from board_space import *
from typing import NamedTuple

class TestBoardSpaces(NamedTuple):
    StartSpace: BoardSpace
    RedSpace_0: BoardSpace
    PurpleSpace_0: BoardSpace
    EndSpace: BoardSpace

class TestBoard:
    def __init__(self) -> None:
        self.board_spaces: TestBoardSpaces = self.generate_test_board()

    def generate_test_board(self) -> TestBoardSpaces:
        return TestBoardSpaces(
            BoardSpace(Color.START, 0),
            BoardSpace(Color.RED, 0),
            BoardSpace(Color.PURPLE, 0),
            BoardSpace(Color.END, 0)
        )