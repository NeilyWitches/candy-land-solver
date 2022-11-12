import board_tests
import deck_tests
import discard_pile_tests
import game_tests
import player_tests

board_tests.test_generate_board()
deck_tests.test_generate_deck()
discard_pile_tests.test_add_card()
game_tests.test_new_game()
game_tests.test_game_over_check()
player_tests.test_is_stuck()
player_tests.test_move_player()