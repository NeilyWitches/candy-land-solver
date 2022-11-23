from game import Game
from game_state import *
from player import Player
from board_space import *
from card import *

game: Game = Game()

if __name__ == '__main__':
    game.start_game()

# example of starting a game from a given game state
# game: Game = Game(GameState(
#     GameStatePlayers(
#         Player(1, BoardSpace(Color.GREEN, 5)),
#         Player(2, BoardSpace(Color.YELLOW, 7, sticky=True)),
#         Player(3, TreatSpace(Treat.FROST)),
#         Player(4, BoardSpace(Color.RED, 20), is_current_player=True),
#     ),
#     DiscardPile({
#         Card(Color.BLUE),
#         Card(Color.GREEN, is_single_block=False),
#         TreatCard(Treat.GUMDROP),
#     })
# ))