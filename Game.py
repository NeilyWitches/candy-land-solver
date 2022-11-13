from typing import Union
from game_state import GameState, GameStatePlayers
from player import Player
from board import Board, BoardSpace, BoardSpaces, Color
from discard_pile import DiscardPile
from deck import Deck
from card import Card

class Game:
    def __init__(self, game_state: Union[GameState, None] = None) -> None:
        self.board: Board = Board()
        self.game_state: GameState
        if game_state is None:
            starting_space: BoardSpace = self.board.board_spaces.StartSpace
            self.game_state = GameState(GameStatePlayers(
                Player(1, starting_space, is_current_player=True),
                Player(2, starting_space),
                Player(3, starting_space),
                Player(4, starting_space),
            ), DiscardPile())
        else:
            self.game_state = game_state

        self.players: GameStatePlayers = self.game_state.players
        self.discard_pile: DiscardPile = self.game_state.discard_pile    

        self.deck: Deck = Deck(self.game_state.discard_pile)

        self.start_game()

    def start_game(self) -> None:
        # while not self.is_game_over():
            # self.display_game_state()
            # self.display_probabilities()
            # self.user_inputs_next_turn()
        pass

    def is_game_over(self) -> bool:
        for player in self.players:
            if player.board_space.color is Color.END:
                return True

        return False

    def apply_drawn_card(self, card: Card) -> None:
        # do not apply the card at all if they are stuck
        if self.current_player().is_stuck(card):
            return

        if card.treat:
            # move the current player to that treat space
            self.move_curr_player_to_treat(card)
        else:
            if card.is_single_block:
                # move current player to the next board space of the card's color
                # self.move_curr_player_to_next(card.color)
                pass
            else:
                pass
                # move the current player to the next board space of the card's color
                # do it again

        # if they land on a short cut space move them to the appropriate space

        # change current player


    # def display_game_state(self):
    def move_curr_player_to_treat(self, treat_card: Card) -> None:
        if treat_card.treat is None:
            raise ValueError("Cannot move a player to a treat space without a treat card")

        # locate the board space
        treat_space: BoardSpace
        board_spaces: BoardSpaces = self.board.board_spaces
        for board_space in board_spaces:
            if board_space.treat == treat_card.treat:
                treat_space = board_space
        
        if treat_space is None:
            raise ValueError("Treat space not found")

        # change the current player's board space to that one
        self.current_player().move_player(treat_space)


    def current_player(self) -> Player:
        for player in self.players:
            if player.is_current_player:
                return player

        raise ValueError("Current player not found")

    def move_curr_player_to_next(self, color: Color) -> None:
        # find the next board space
        # the board space whose position is one more than the curr player's position
        curr_player_position: int = self.current_player().board_space.position
        next_position: int = curr_player_position + 1
        # locate the boardspace with this position that has the same color as the players current board space
        next_board_space: BoardSpace
        board_space_not_found: bool = True
        for board_space in self.board.board_spaces:
            if board_space.color == color and board_space.position == next_position:
                next_board_space = board_space
                board_space_not_found = False

        # move curr player to that board space
        if board_space_not_found:
            self.current_player().move_player(self.board.board_spaces.EndSpace)
            return

        self.current_player().move_player(next_board_space)