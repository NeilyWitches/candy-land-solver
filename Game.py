from typing import Union
from game_state import *
from player import *
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
        while not self.is_game_over():
            try:
                self.display_game_state()
                # self.display_probabilities()
                user_input: str = self.user_inputs_next_card()
                if user_input == "help":
                    self.help_with_input()
                    continue
                if user_input == "quit":
                    return
                card = self.deck.find_card(user_input)
                self.take_turn(card)

                if self.is_game_over():
                    self.display_game_state()
            except Exception as e:
                print("\n")
                print(" " + "-"*len(str(e)))
                print("|" + str(e) + "|")
                print(" " + "-"*len(str(e)))
                print("\n")
                print("Press 'return' to go back to the game and try another input")
                input()

    def help_with_input(self):
        print("\n")
        print("                                            HELP: \n")
        print("- To enter a basic color card, type the first letter of the name of the color (in lower case)")
        print("  - once if the card has only 1 square of the color")
        print("  - twice if the card has 2 squares of that color.")
        print("  - For example, if you drew a single square purple card, you would type 'p'.") 
        print("  - 'If you drew a double square red card, you would type 'rr'.")
        print("- To enter a treat card, type in the full name of the treat in all lower case.")
        print("  - The treats, in order from the beginning of the board map to the end, are:")
        print("  - ['plum', 'candy cane', 'gumdrop', 'nut', 'lollipop', 'frost']") 
        print("- Press 'return' to go back to the game.")
        input()

    def user_inputs_next_card(self) -> str:
        user_input: str

        print("\n")
        print("Please enter the next drawn card. Type 'help' for help, or 'quit' to quit.")
        user_input = input()

        return user_input

    def display_game_state(self) -> None:
        player_1: Player = self.players.Player_1
        player_2: Player = self.players.Player_2
        player_3: Player = self.players.Player_3
        player_4: Player = self.players.Player_4

        player_1_current_player: str = "(current player)" if player_1.is_current_player else "                "
        player_2_current_player: str = "(current player)" if player_2.is_current_player else "                "
        player_3_current_player: str = "(current player)" if player_3.is_current_player else "                "
        player_4_current_player: str = "(current player)" if player_4.is_current_player else "                "

        def format_position(board_space: BoardSpace) -> str:
            position: int = board_space.position + 1
            if board_space.color == Color.START or board_space.treat or board_space.color == Color.END:
                return ""
            if position == 1:
                return "1st "
            if position == 2:
                return "2nd "
            if position == 3:
                return "3rd "
            if position == 21:
                return "21st "
            else:
                return str(position) + "th "

        def format_shortcut(player: Player) -> str:
            if player.shortcut_taken:
                return f"(through {player.shortcut_taken.name})"
            else:
                return ""

        def format_name(board_space: BoardSpace) -> str:
            if board_space.treat:
                return board_space.treat.name
            else:
                if board_space.color == Color.END:
                    return board_space.color.name + " (WINNER!)"

                return board_space.color.name

        def format_sticky(player: Player) -> str:
            if player.stuck_state == StuckState.ON_STICKY_SPACE:
                return "(sticky)"
            if player.stuck_state == StuckState.FAILED_TO_GET_UNSTUCK:
                return "(STUCK!)"
            if player.stuck_state == StuckState.SUCCEEDED_TO_GET_UNSTUCK:
                return "(ESCAPED!)" 

            return ""   

        def format_board_space(player: Player) -> str:
            player_board_space: str = format_position(player.board_space)
            player_board_space = player_board_space + format_name(player.board_space) + " "
            player_board_space = player_board_space + format_shortcut(player)
            player_board_space = player_board_space + format_sticky(player)
            return player_board_space + (35 - len(player_board_space))*" "

            # 10th Purple (through Rainbow Trail)

        print("+--------------------+-------------------------------------+-----------------------+")
        print("|                    |                                     |                       |")
        print("|       Player       |          Space on the board         | Proability of winning |")
        print("|                    |                                     |                       |")
        print("+--------------------+-------------------------------------+-----------------------+")
        print(f"| 1 {player_1_current_player} | {format_board_space(player_1)} | 33.68 %               |")
        print("+--------------------+-------------------------------------+-----------------------+")
        print(f"| 2 {player_2_current_player} | {format_board_space(player_2)} | 14.21 %               |")
        print("+--------------------+-------------------------------------+-----------------------+")
        print(f"| 3 {player_3_current_player} | {format_board_space(player_3)} | 11.90 %               |")
        print("+--------------------+-------------------------------------+-----------------------+")
        print(f"| 4 {player_4_current_player} | {format_board_space(player_4)} | 55.00 %               |")
        print("+--------------------+-------------------------------------+-----------------------+")
    
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
        
        current_player.update_shortcut_taken(current_player.board_space.shortcut)
        
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
        current_player: Player = self.current_player()
        current_player.move_player(treat_space)

        current_player.update_shortcut_taken(None)

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

        curr_player.update_shortcut_taken(None)

        for i in range(curr_player_board_space_idx + 1, len(self.board.board_spaces)):
            if self.board.board_spaces[i].color == Color.END:
                curr_player.move_player(self.board.board_spaces.EndSpace)
            elif self.board.board_spaces[i].color == color:
                curr_player.move_player(self.board.board_spaces[i])
                return