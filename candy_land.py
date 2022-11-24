from game import Game
from game_state import *
from player import Player
from board_space import *
from card import *

# game: Game = Game()

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

game: Game = Game(GameState(
    GameStatePlayers(
        Player(1, BoardSpace(Color.PURPLE, 21), is_current_player=True),
        Player(2, BoardSpace(Color.PURPLE, 21)),
        Player(3, BoardSpace(Color.PURPLE, 21)),
        Player(4, BoardSpace(Color.PURPLE, 21)),
    ),
    DiscardPile({
        Card(Color.BLUE),
        Card(Color.GREEN, is_single_block=False),
        TreatCard(Treat.GUMDROP),
    })
))

if __name__ == '__main__':
    game.start_game()