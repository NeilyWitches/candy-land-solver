# given a game state, calculate each player's probability of winning
from test_game import TestGame
from board_space import Color

test_game = TestGame()
total = {"games": 0}

# total.games = 3
# board = [start, red, purple, end]
#                        1
#                  2c

# deck = [r1, r2, r3, p1, p2]
#          i
# deck = [r1, r2, r3, p1, p2]
#              i
# deck = [r1, r2, r3, p1, p2]
#                          i
# deck = [r1, r2, r3, p1, p2]
#                      i

# discard = {r1, r2, p2}


def prob():
    if test_game.test_players[0].board_space.color == Color.END:
        total["games"] += 1
        return 1

    if test_game.test_players[1].board_space.color == Color.END:
        total["games"] += 1
        return 0

    wins = 0
    # wins = 0
    # wins = 0
    # wins = 2
    # wins = 0
    for card in test_game.test_deck:
        if card not in test_game.test_discard_pile:
            board_space_before = test_game.current_test_player().board_space
            # board_space_before = start
            # board_space_before = start
            # board_space_before = red
            # board_space_before = red
            test_game.take_test_turn(card)
            wins += prob()
            test_game.undo_test_turn(board_space_before, card)

    return wins

print("prob: ", prob())
print("total games: ", total["games"])