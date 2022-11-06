from BoardSpace import BoardSpace

class Player:
    def __init__(self, player_number: int, board_space: BoardSpace) -> None:
        self.player_number: int = player_number
        self.board_space: BoardSpace = board_space