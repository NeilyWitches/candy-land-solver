from board import BoardSpace

class Player:
    def __init__(self, player_number: int, board_space: BoardSpace, is_current_player: bool = False) -> None:
        self.player_number: int = player_number
        self.board_space: BoardSpace = board_space
        self.is_current_player: bool = is_current_player