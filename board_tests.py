from board import Board, BoardSpaces, BoardSpace
# from board_space import BoardSpace

def test_generate_board() -> None:
    board: Board = Board()
    board_spaces: BoardSpaces = board.board_spaces
    skips_or_repeats: bool = False
    for idx, board_space in enumerate(board_spaces):
        if idx is not board_space.position:
            skips_or_repeats = True
            break

    assert skips_or_repeats == False, "board skips or repeats positions"