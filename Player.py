from board_space import *
from card import Card

class StuckState(Enum):
    NOT_ON_STICKY_SPACE = 1
    ON_STICKY_SPACE = 2
    FAILED_TO_GET_UNSTUCK = 3
    SUCCEEDED_TO_GET_UNSTUCK = 4

class Player:
    def __init__(self, player_number: int, board_space: BoardSpace, is_current_player: bool = False) -> None:
        self.player_number: int = player_number
        self.board_space: BoardSpace = board_space
        self.is_current_player: bool = is_current_player
        self.shortcut_taken: Union[Shortcut, None] = None
        self.stuck_state: StuckState = StuckState.NOT_ON_STICKY_SPACE

    def copy(self) -> 'Player':
        copy: Player =  Player(
            self.player_number,
            self.board_space.copy(),
            self.is_current_player
        )
        copy.shortcut_taken = self.shortcut_taken
        copy.stuck_state = self.stuck_state
        return copy

    def is_stuck(self, card: Card) -> bool:
        if not self.is_current_player:
            raise ValueError("Should only be checking if the CURRENT player is stuck")

        if not self.board_space.sticky:
            self.stuck_state = StuckState.NOT_ON_STICKY_SPACE
            return False

        self.stuck_state = StuckState.ON_STICKY_SPACE
        
        if self.board_space.color == card.color:
            self.stuck_state = StuckState.SUCCEEDED_TO_GET_UNSTUCK
            return False

        self.stuck_state = StuckState.FAILED_TO_GET_UNSTUCK
        return True

    def move_player(self, board_space: BoardSpace) -> None:
        # only move the player if they are the current player
        if not self.is_current_player:
            raise ValueError("Can only move the current player")

        old_board_space: BoardSpace = self.board_space
        self.board_space = board_space
        if board_space.sticky:
            if old_board_space.sticky:
                self.stuck_state = StuckState.FAILED_TO_GET_UNSTUCK
            else:
                self.stuck_state = StuckState.ON_STICKY_SPACE
        else:
            if old_board_space.sticky:
                self.stuck_state = StuckState.SUCCEEDED_TO_GET_UNSTUCK
            else:
                self.stuck_state = StuckState.NOT_ON_STICKY_SPACE

    def toggle_is_current_player(self) -> None:
        self.is_current_player = not self.is_current_player

    def update_shortcut_taken(self, shortcut_taken: Union[Shortcut, None]) -> None:
        self.shortcut_taken = shortcut_taken