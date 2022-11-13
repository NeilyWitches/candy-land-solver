from board import Board, BoardSpaces, Color
from typing import Dict

def test_generate_board() -> None:

    board: Board = Board()
    board_spaces: BoardSpaces = board.board_spaces
    counters: Dict[Color, int] = {
        Color.START: 0,
        Color.RED: 0,
        Color.PURPLE: 0,
        Color.YELLOW: 0,
        Color.BLUE: 0,
        Color.ORANGE: 0,
        Color.GREEN: 0,
        Color.PINK: 0,
        Color.END: 0,
    }
    
    for board_space in board_spaces:
        assert counters[board_space.color] == board_space.position, "Skipped or repeated position"
        counters[board_space.color] += 1

    assert counters[Color.START] == 1, "Wrong number of start spaces"
    assert counters[Color.RED] == 22, "Wrong number of red spaces"
    assert counters[Color.PURPLE] == 22, "Wrong number of purple spaces"
    assert counters[Color.YELLOW] == 21, "Wrong number of yellow spaces"
    assert counters[Color.BLUE] == 21, "Wrong number of blue spaces"
    assert counters[Color.ORANGE] == 21, "Wrong number of orange spaces"
    assert counters[Color.GREEN] == 21, "Wrong number of green spaces"
    assert counters[Color.PINK] == 6, "Wrong number of treat spaces"
    assert counters[Color.END] == 1, "Wrong number of end spaces"