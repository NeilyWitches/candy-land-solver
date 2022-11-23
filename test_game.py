from game import Game
from test_board import *
from player import *
from typing import Tuple, List, Set

class TestGame(Game):
    def __init__(self) -> None:
        self.test_board: TestBoard = TestBoard()
        starting_space: BoardSpace = self.test_board.board_spaces.StartSpace
        self.test_players: Tuple[Player, Player] =  (
            Player(1, starting_space, is_current_player=True),
            Player(2, starting_space)
        )
        self.test_discard_pile: Set[Card] = set()
        self.test_deck: List[Card] = [
            Card(Color.RED), Card(Color.RED), Card(Color.RED),
            Card(Color.PURPLE), Card(Color.PURPLE), 
        ]

    def take_test_turn(self, card: Card) -> None:
        self.move_curr_test_player(card.color)
        self.test_discard_pile.add(card)
        if self.current_test_player().board_space.color != Color.END:
            self.change_test_players()

    def undo_test_turn(self, board_space: BoardSpace, card: Card) -> None:
        if self.current_test_player().board_space.color != Color.END:
            self.change_test_players()
        self.current_test_player().move_player(board_space)
        self.test_discard_pile.remove(card)

    def next_test_player(self) -> Player:
        next_player_number: int = self.current_test_player().player_number % 2 + 1
        for player in self.test_players:
            if player.player_number == next_player_number:
                return player

        return Player(3, BoardSpace(Color.GREEN, 0))

    def change_test_players(self) -> None:
        current_player: Player = self.current_test_player()
        next_player: Player = self.next_test_player()
        current_player.toggle_is_current_player()
        next_player.toggle_is_current_player()

    def current_test_player(self) -> Player:
        for player in self.test_players:
            if player.is_current_player:
                return player

        return Player(3, BoardSpace(Color.GREEN, 0))

    def move_curr_test_player(self, color: Color) -> None:
        curr_player_board_space_idx: int
        curr_player: Player = self.current_test_player()
        for i, board_space in enumerate(self.test_board.board_spaces):
            if board_space == curr_player.board_space:
                curr_player_board_space_idx = i
        
        for i in range(curr_player_board_space_idx + 1, len(self.test_board.board_spaces)):
            if self.test_board.board_spaces[i].color == Color.END:
                curr_player.move_player(self.test_board.board_spaces.EndSpace)
            elif self.test_board.board_spaces[i].color == color:
                curr_player.move_player(self.test_board.board_spaces[i])
                return
