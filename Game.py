from typing import Union
from game_state import *
from player import Player
from board import Board, BoardSpaces
from discard_pile import DiscardPile
from deck import Deck
from card import Card
from board_space import *

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
            self.put_players_on_board()

        self.players: GameStatePlayers = self.game_state.players
        self.discard_pile: DiscardPile = self.game_state.discard_pile    

        self.deck: Deck = Deck(self.game_state.discard_pile)

        self.start_game()

    def put_players_on_board(self) -> None:
        num_players_placed: int = 0
        for _ in range(4):
            current_player: Player = self.current_player()
            for board_space in self.board.board_spaces:
                if current_player.board_space.color == board_space.color and current_player.board_space.position == board_space.position and current_player.board_space.sticky == board_space.sticky and current_player.board_space.shortcut == board_space.shortcut and current_player.board_space.treat == board_space.treat:
                    current_player.move_player(board_space)
                    num_players_placed += 1
                    self.change_players()

        if num_players_placed < 4:
            raise ValueError("Not all players were put on the board")

    def start_game(self) -> None:
        # while not self.is_game_over():
            # self.display_game_state()
            # self.display_probabilities()
            # input = self.user_inputs_next_turn()
            # card = game.deck.find_card(input)
            # self.take_turn(card)
        pass
    
    def take_turn(self, card: Card) -> None:
        self.deck.draw_card(card)
        self.apply_drawn_card(card)
        self.discard_pile.add_card(card)
        self.change_players()

    def is_game_over(self) -> bool:
        for player in self.players:
            if player.board_space.color is Color.END:
                return True

        return False

    def apply_drawn_card(self, card: Card) -> None:
        # do not apply the card at all if the current player is stuck
        if self.current_player().is_stuck(card):
            return

        if card.treat:
            # move the current player to that treat space
            self.move_curr_player_to_treat(card.treat)
        else:
            if card.is_single_block:
                # move current player to the next board space of the card's color
                self.move_curr_player_to_next_color(card.color)
            else:
                for _ in range(2):
                    self.move_curr_player_to_next_color(card.color)

        # if they land on a short cut space move them to the appropriate space
        if self.current_player().board_space.shortcut:
            self.take_curr_player_through_shortcut()
    
    def take_curr_player_through_shortcut(self) -> None:
        current_player: Player = self.current_player()

        if current_player.board_space.shortcut is None:
            raise ValueError("only the current player can go through a shortcut")
        
        if current_player.board_space.shortcut == Shortcut.RAINBOW_TRAIL:
            current_player.move_player(self.board.board_spaces.PurpleSpace_9)
        
        if current_player.board_space.shortcut == Shortcut.GUMDROP_PASS:
            current_player.move_player(self.board.board_spaces.PurpleSpace_7)

    def move_curr_player_to_treat(self, treat: Treat) -> None:
        # locate the board space
        treat_space: BoardSpace
        board_spaces: BoardSpaces = self.board.board_spaces
        for board_space in board_spaces:
            if board_space.treat == treat:
                treat_space = board_space
        
        if treat_space is None:
            raise ValueError("Treat space not found")

        # change the current player's board space to that one
        self.current_player().move_player(treat_space)


    def current_player(self) -> Player:
        for player in self.game_state.players:
            if player.is_current_player:
                return player

        raise ValueError("Current player not found")

    def next_player(self) -> Player:
        next_player_number: int = self.current_player().player_number % 4 + 1
        for player in self.game_state.players:
            if player.player_number == next_player_number:
                return player
        
        raise ValueError("Next player not found")

    def change_players(self) -> None:
        current_player: Player = self.current_player()
        next_player: Player = self.next_player()
        current_player.toggle_is_current_player()
        next_player.toggle_is_current_player()

    def move_curr_player_to_next_color(self, color: Color) -> None:
        curr_player_board_space_idx: int
        curr_player: Player = self.current_player()
        space_not_found: bool = True
        for i, board_space in enumerate(self.board.board_spaces):
            if board_space == curr_player.board_space:
                curr_player_board_space_idx = i
                space_not_found = False

        if space_not_found:
            raise ValueError("The current player's board space was not found on the board")

        for i in range(curr_player_board_space_idx + 1, len(self.board.board_spaces)):
            if self.board.board_spaces[i].color == Color.END:
                curr_player.move_player(self.board.board_spaces.EndSpace)
            elif self.board.board_spaces[i].color == color:
                curr_player.move_player(self.board.board_spaces[i])
                return