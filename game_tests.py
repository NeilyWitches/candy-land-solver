from game import *
from player import Player
from board import *
from discard_pile import DiscardPile
from card import *
from typing import Set, List

def test_new_game() -> None:
    # creating a new game without a game state, initializes the game
    # with the correct game state
    game: Game = Game()

    players: Players = game.players
    discard_pile: DiscardPile = game.discard_pile

    correct_players: Players = Players(
        Player(1, game.board.board_spaces.StartSpace, is_current_player=True),
        Player(2, game.board.board_spaces.StartSpace),
        Player(3, game.board.board_spaces.StartSpace),
        Player(4, game.board.board_spaces.StartSpace),
    )
    correct_discard_pile: DiscardPile = DiscardPile()

    assert has_correct_players(players, correct_players) == True, "The game state has incorrect players"
    assert has_correct_discard_pile(discard_pile, correct_discard_pile) == True, "The game state has an incorrect discard pile"

def test_create_copy() -> None:
    # the memory address of the copy should be different from the original
    game_original: Game = Game()
    game_copy: Game = game_original.copy()

    assert game_original != game_copy, "The memory addresses of the copy should be different from the original, but it is not"

    # the game copy's board should have a different memory address than the original game's board
    assert game_copy.board != game_original.board, "The boards are the same, but they should be different"

    # a single board space should be different
    assert game_copy.board.board_spaces.StartSpace != game_original.board.board_spaces.StartSpace, "The start space of the copy should be different from the original, but it is not"
    # but their attributes should be the same
    assert game_original.board.board_spaces.StartSpace.color == game_copy.board.board_spaces.StartSpace.color, "The color of the copy board space should be the same as the original, but it is not"
    assert game_original.board.board_spaces.StartSpace.position == game_copy.board.board_spaces.StartSpace.position, "The position of the copy board space should be the same as the original, but it is not"
    assert game_original.board.board_spaces.StickySpace_0.sticky == game_copy.board.board_spaces.StickySpace_0.sticky, "The sticky attribute of the copy board space should be the same as the original, but it is not"
    assert game_original.board.board_spaces.GumdropPass.shortcut == game_copy.board.board_spaces.GumdropPass.shortcut, "The shortcut attribute of the copy board space should be the same as the original, but it is not"
    assert game_original.board.board_spaces.Plumb.treat == game_copy.board.board_spaces.Plumb.treat, "The treat attribute of the copy board space should be the same as the original board space, but it is not"

    # a single player should be different
    assert game_copy.players.Player_1 != game_original.players.Player_1, "Player 1 of the copy should be different from player 1 of the original, but it is not"
    # but their attributes should be the same
    assert game_original.players.Player_1.player_number == game_copy.players.Player_1.player_number, "The player numbers of the copy player should be the same as the original player, but it is not"
    assert game_original.players.Player_1.is_current_player == game_copy.players.Player_1.is_current_player, "The current player attribute of the copy player should be the same as the original player, but it is not"
    assert game_original.players.Player_2.is_current_player == game_copy.players.Player_2.is_current_player, "The current plalyer attirubte of the copy player for player 2 should be the same as the original player 2, but is not"
    assert game_original.players.Player_1.shortcut_taken == game_copy.players.Player_1.shortcut_taken, "The shortcut taken attribute of the copy should be the same as the original, but it is not"
    assert game_original.players.Player_1.stuck_state == game_copy.players.Player_1.stuck_state, "The stuck state attribute of the copy player should be the same as the original, but it is not"
    
    # a single player's board space should be different
    assert game_copy.players.Player_1.board_space != game_original.players.Player_1.board_space, "The board space of a single player copy should be different from the original, but it is the same"
    # but the attributes of those board spaces should be the same
    assert game_original.players.Player_1.board_space.color == game_copy.players.Player_1.board_space.color, "The color of the copy board space of a single player should be the same as the original, but it is not"
    assert game_original.players.Player_1.board_space.position == game_copy.players.Player_1.board_space.position, "The position of the copy board space of a single player should be the same as the original, but it is not"
    assert game_original.players.Player_1.board_space.sticky == game_copy.players.Player_1.board_space.sticky, "The sticky attribute of the copy board space of a single player should be the same as the original, but it is not"
    assert game_original.players.Player_1.board_space.shortcut == game_copy.players.Player_1.board_space.shortcut, "The shortcut attribute of the copy board space of a single player should be the same as the original, but it is not"
    assert game_original.players.Player_1.board_space.treat == game_copy.players.Player_1.board_space.treat, "The treat attribute of the copy board space of a player should be the same as the original board space, but it is not"

    # the discard piles should differ
    assert game_copy.discard_pile != game_original.discard_pile, "The copy's discard pile should be different from the original, but it is not"

    # a single card from the decks should differ
    original_card: Card = game_original.deck.find_card("nut")
    copy_card: Card = game_copy.deck.find_card("nut")
    assert original_card != copy_card, "The two nut cards should differ, but they don't"
    # but their attributes should be the same
    assert original_card.is_single_block == copy_card.is_single_block, "The original card should have the same is single block attribute as the copy card, but it does not"
    assert original_card.color == copy_card.color, "The original card should be the same color as the copy card, but is not"
    assert original_card.treat == copy_card.treat, "The original card should have the same treat attribute as the copy card, but it does not"

    # a single card from the discard piles should differ
    game_original.take_turn(original_card)
    game_copy.take_turn(copy_card)
    assert original_card in game_original.discard_pile.cards, "The original card should now be in the original discard pile, but it is not"
    assert copy_card in game_copy.discard_pile.cards, "The copy card should now be in the original discard pile, but it is not"
    assert original_card not in game_copy.discard_pile.cards, "The original card should NOT be in the copy discard pile, but it is"
    assert copy_card not in game_original.discard_pile.cards, "The copy card should NOT be in the original discard pile, but it is"

def test_copy_players() -> None:
    game: Game = Game()
    original_players: Players = game.players
    copy_players: Players = game.copy_players()

    # a single player should be different
    assert original_players.Player_1 != copy_players.Player_1, "Player 1 copy should differ from player 1 original, but doesn't" 
    # but their attributes should be the same
    assert original_players.Player_1.player_number == copy_players.Player_1.player_number, "The player numbers of the copy player should be the same as the original player, but it is not"
    assert original_players.Player_1.is_current_player == copy_players.Player_1.is_current_player, "The current player attribute of the copy player should be the same as the original player, but it is not"
    assert original_players.Player_2.is_current_player == copy_players.Player_2.is_current_player, "The current player attribute of the copy player for player 2 should be the same as the original player 2, but is not"
    assert original_players.Player_1.shortcut_taken == copy_players.Player_1.shortcut_taken, "The shortcut taken attribute of the copy should be the same as the original, but it is not"
    assert original_players.Player_1.stuck_state == copy_players.Player_1.stuck_state, "The stuck state attribute of the copy player should be the same as the original, but it is not"

    # a single player's board space should be different
    assert copy_players.Player_1.board_space != original_players.Player_1.board_space, "The board space of a single player copy should be different from the original, but it is the same"
    # but the attributes of those board spaces should be the same
    assert original_players.Player_1.board_space.color == copy_players.Player_1.board_space.color, "The color of the copy board space of a single player should be the same as the original, but it is not"
    assert original_players.Player_1.board_space.position == copy_players.Player_1.board_space.position, "The position of the copy board space of a single player should be the same as the original, but it is not"
    assert original_players.Player_1.board_space.sticky == copy_players.Player_1.board_space.sticky, "The sticky attribute of the copy board space of a single player should be the same as the original, but it is not"
    assert original_players.Player_1.board_space.shortcut == copy_players.Player_1.board_space.shortcut, "The shortcut attribute of the copy board space of a single player should be the same as the original, but it is not"
    assert original_players.Player_1.board_space.treat == copy_players.Player_1.board_space.treat, "The treat attribute of the copy board space of a player should be the same as the original board space, but it is not"

def has_correct_players(players: Players, correct_players: Players) -> bool:
    for i in range(4):
        if players[i].player_number != correct_players[i].player_number or players[i].board_space.color != correct_players[i].board_space.color or correct_players[i].board_space.position != players[i].board_space.position or correct_players[i].is_current_player != players[i].is_current_player:
            return False
    return True

def has_correct_discard_pile(discard_pile: DiscardPile, correct_discard_pile: DiscardPile) -> bool:
    if len(discard_pile.cards) != len(correct_discard_pile.cards):
        return False

    bucket: Set = set()
    for card in discard_pile.cards:
        for correct_card in correct_discard_pile.cards:
            if correct_card not in bucket and card.is_single_block == correct_card.is_single_block and card.color == correct_card.color and card.treat == correct_card.treat:
                bucket.add(correct_card)

    return len(bucket) == len(discard_pile.cards)    

def test_game_over() -> None:
    # it should know the game is not over when none of the players 
    # have made it to the end yet

    game: Game = Game()
    game_over = game.is_game_over()

    assert game_over == False, "The game should not be over, but it is"

    # take turns until player 1 wins
    cards: List[Card] = []

    # cards = []

    for card in game.deck.cards:
        if card.treat == Treat.FROST:
            cards.append(card)
            break

    #             0
    # cards = [frost]

    cards_count: int = 0
    for card in game.deck.cards:
        is_double_purple: bool = card.is_single_block == False and card.color == Color.PURPLE
        is_frost: bool = card.treat == Treat.FROST
        if not is_double_purple and not is_frost:
            cards.append(card)
            cards_count += 1
        if cards_count == 9:
            break

    #            0     1    2        3    4     5     6     7     8    9
    # cards = [frost, card, card, card, card, card, card, card, card, card]

    cards_count = 0
    for card in game.deck.cards:
        if card.color == Color.PURPLE and card.is_single_block == False:
            cards.append(card)
            cards_count += 1
        if cards_count == 3:
            break

    #            0     1    2        3    4     5     6     7     8    9       10            11               12
    # cards = [frost, card, card, card, card, card, card, card, card, card, double purple, double purple, double purple]

    game.take_turn(cards[0])
    for i in range(1, 4):
        game.take_turn(cards[i])

    game.take_turn(cards.pop())

    #            0     1    2        3    4     5     6     7     8    9       10            11      
    # cards = [frost, card, card, card, card, card, card, card, card, card, double purple, double purple]

    for i in range(4, 7):
        game.take_turn(cards[i])

    game.take_turn(cards.pop())
    #            0     1    2        3    4     5     6     7     8    9       10          
    # cards = [frost, card, card, card, card, card, card, card, card, card, double purple]

    for i in range(7, 10):
        game.take_turn(cards[i])

    game.take_turn(cards.pop())
    #            0     1    2        3    4     5     6     7     8    9    
    # cards = [frost, card, card, card, card, card, card, card, card, card]

    assert game.players.Player_1.board_space.color == Color.END, "Player 1 should have made it to the end, but they did not"
    assert game.is_game_over() == True, "The game should be over, but it is not"
    
def test_move_curr_player_to_treat() -> None:
    # only the current player should be moved
    game: Game = Game()
    current_player: Player = game.current_player()
    player_2: Player = game.players.Player_2
    player_3: Player = game.players.Player_3
    # make sure the current player is not player 2
    assert player_2 != current_player, "The current player should not be player 2, but they are"
    # all of the players start at the same board space, i.e. the start space
    assert current_player.board_space == player_2.board_space, "The current player and player 2 should have started at the same board space, but they did not"
    # after the current player has been moved,
    game.move_curr_player_to_treat(Treat.CANDY_CANE)
    # the current player and player 2 should not be on the same board space
    assert current_player.board_space != player_2.board_space, "The current player and player 2 should not be on the same board space, but they are"
    # but player 2 and player 3 should still be on the start space
    assert player_2.board_space == player_3.board_space, "Player 2 and Player 3 should be on the same board space, but they are not"
    assert player_3.board_space == game.board.board_spaces.StartSpace, "Player 3 should be on the start space but they are not"

    # the current player should be moved to the correct treat space
    assert current_player.board_space == game.board.board_spaces.CandyCane, "The current player is on the wrong board space"

def test_current_player() -> None:
    # finds the current player
    game: Game = Game()
    assert game.current_player() == game.players.Player_1, "The current player should be player 1, but they are not"

def test_next_player() -> None:
    # find the next player
    game: Game = Game()
    assert game.next_player() == game.players.Player_2, "player 2 should be the next player, but is not"
    assert game.next_player() != game.players.Player_1, "player 1 should not be the next player"
    assert game.next_player() != game.players.Player_3, "player 3 should not be the next player"
    assert game.next_player() != game.players.Player_4, "player 4 should not be the next player"

    game.players.Player_1.toggle_is_current_player()
    game.players.Player_4.toggle_is_current_player()

    assert game.next_player() == game.players.Player_1, "player 1 should be the next player, but is not"
    assert game.next_player() != game.players.Player_2, "player 2 should not be the next player"
    assert game.next_player() != game.players.Player_3, "player 3 should not be the next player"
    assert game.next_player() != game.players.Player_4, "player 4 should not be the next player"

def test_prev_player() -> None:
    # finds the previous player
    game: Game

    game = Game()
    assert game.prev_player() != game.players.Player_1, "player 1 should not be the prev player"
    assert game.prev_player() != game.players.Player_2, "player 2 should not be the prev player"
    assert game.prev_player() != game.players.Player_3, "player 3 should not be the prev player"
    assert game.prev_player() == game.players.Player_4, "player 4 should be the prev player"

    game.players.Player_1.toggle_is_current_player()
    game.players.Player_4.toggle_is_current_player()

    assert game.prev_player() != game.players.Player_1, "player 1 should not be the prev player"
    assert game.prev_player() != game.players.Player_2, "player 2 should not be the prev player"
    assert game.prev_player() == game.players.Player_3, "player 3 should be the prev player"
    assert game.prev_player() != game.players.Player_4, "player 4 should not be the prev player"

def test_move_curr_player_to_next_color() -> None:
    # it should move the current_player and not some other player
    game: Game = Game()
    current_player: Player = game.current_player()
    current_player.move_player(game.board.board_spaces.RedSpace_0)
    other_player: Player = game.players.Player_2
    curr_player_board_space_before: BoardSpace = current_player.board_space
    other_player_board_space_before: BoardSpace = other_player.board_space

    game.move_curr_player_to_next_color(Color.BLUE)

    curr_player_board_space_after: BoardSpace = current_player.board_space
    other_player_board_space_after: BoardSpace = other_player.board_space

    assert other_player_board_space_before == other_player_board_space_after, "A player that was not the current player was moved"
    assert curr_player_board_space_before != curr_player_board_space_after, "The current player did not move, but they should have"

    # it should move the current_player to the next board space of the correct color
    assert curr_player_board_space_after.color == Color.BLUE, "The player moved to the wrong color"

    # it should move the current_player to the correct position
    assert curr_player_board_space_after.position == 0, "The player moved to the wrong position"

    # the current player should not have stayed in the same spot
    # especially if they were on that color
    game.move_curr_player_to_next_color(Color.BLUE)
    assert game.current_player().board_space != curr_player_board_space_after, "the current player stayed in the same spot, but they should have moved"
    assert game.current_player().board_space.color == Color.BLUE, "the current player landed on the wrong color"
    assert game.current_player().board_space.position == 1, "the current player landed on the wrong position"

    # the game is over if the current player makes it to the end
    last_space_before_end: BoardSpace = game.board.board_spaces.PurpleSpace_21
    game.current_player().move_player(last_space_before_end)
    game.move_curr_player_to_next_color(Color.ORANGE)

    assert game.is_game_over() == True, "The game should be over, but is not"

def test_put_players_on_board() -> None:
    # if you create a game, all of the players'
    # board spaces should be the actual board spaces on the board
    game: Game = Game()
    for player in game.players:
        assert player.board_space in game.board.board_spaces, "A player's board space was not found on the board for a game with an empty game state"

def test_change_players() -> None:
    # if player 1 is the current player, when you change players, player 2 should be the current player
    game: Game = Game()
    players: Players = game.players
    player_1: Player = players.Player_1
    player_2: Player = players.Player_2
    player_3: Player = players.Player_3
    player_4: Player = players.Player_4

    assert player_1.is_current_player == True, "player 1 should be current player but is not"
    assert player_2.is_current_player == False, "player 2 should not be current player"
    assert player_3.is_current_player == False, "player 3 should not be current player"
    assert player_4.is_current_player == False, "player 4 should not be current player"

    game.change_players()

    assert player_1.is_current_player == False, "player 1 should not be current player"
    assert player_2.is_current_player == True, "player 2 should be current player but is not"
    assert player_3.is_current_player == False, "player 3 should not be current player"
    assert player_4.is_current_player == False, "player 4 should not be current player"

    # make sure it works for a full rotation
    game.change_players()
    assert player_1.is_current_player == False, "player 1 should not be current player"
    assert player_2.is_current_player == False, "player 2 should not be current player"
    assert player_3.is_current_player == True, "player 3 should be current player, but is not"
    assert player_4.is_current_player == False, "player 4 should not be current player"

    game.change_players()
    assert player_1.is_current_player == False, "player 1 should not be current player"
    assert player_2.is_current_player == False, "player 2 should not be current player"
    assert player_3.is_current_player == False, "player 3 should not be current player"
    assert player_4.is_current_player == True, "player 4 should be current player, but is not"

    game.change_players()

    assert player_1.is_current_player == True, "player 1 should be current player, but is not"
    assert player_2.is_current_player == False, "player 2 should not be current player"
    assert player_3.is_current_player == False, "player 3 should not be current player"
    assert player_4.is_current_player == False, "player 4 should not be current player"


def test_take_curr_player_through_shortcut() -> None:
    # if the current player is on rainbow trail
    game: Game = Game()
    player: Player = game.players.Player_1
    game.move_curr_player_to_next_color(Color.ORANGE)
    assert player.board_space == game.board.board_spaces.RainbowTrail, "The player should be on rainbow trail, but they are not"
    # after they take the shortcut,
    game.take_curr_player_through_shortcut()
    # they should end up at the correct board space:
    assert player.board_space == game.board.board_spaces.PurpleSpace_9, "The player should be on purple space 9, but they are not"

    # checking the other shortcut, gumdrop pass
    game.move_curr_player_to_treat(Treat.PLUM)
    for _ in range(4):
        game.move_curr_player_to_next_color(Color.PURPLE)

    assert player.board_space == game.board.board_spaces.GumdropPass, "The player should be on gumdrop pass, but they are not"
    game.take_curr_player_through_shortcut()

    assert player.board_space == game.board.board_spaces.PurpleSpace_7, "The player should be on purple space 7, but they are not"

def test_apply_drawn_card() -> None:
    game: Game = Game()

    game.players.Player_1.move_player(game.board.board_spaces.CandyCane)
    game.change_players()
    game.players.Player_2.move_player(game.board.board_spaces.BlueSpace_14)
    game.change_players()
    game.players.Player_3.move_player(game.board.board_spaces.StartSpace)
    game.change_players()
    game.players.Player_4.move_player(game.board.board_spaces.StickySpace_2)

    # does not apply the card at all if the current player is stuck
    assert game.current_player().board_space == game.board.board_spaces.StickySpace_2, "The current player should be on sticky space 2, but they are not"
    game.apply_drawn_card(Card(Color.YELLOW, is_single_block=False))
    assert game.board.board_spaces.StickySpace_2 == game.players.Player_4.board_space, "Player 4's should not have moved because they are stuck, but they did"

    # successfully unsticks the player if appropriate
    game.apply_drawn_card(Card(Color.RED, is_single_block=False))
    assert game.current_player().board_space == game.board.board_spaces.RedSpace_21, "Player 4 should have become unstuck, but they remained on the same board space"

    # successfully applies a treat card
    game.apply_drawn_card(TreatCard(Treat.LOLLIPOP))
    assert game.current_player().board_space == game.board.board_spaces.Lollipop, "Player 4 should be on the lollipop space, but they are not"

    # correctly applies a single block card
    game.apply_drawn_card(Card(Color.ORANGE))
    assert game.players.Player_4.board_space == game.board.board_spaces.OrangeSpace_15, "The current player should be on orange space 15, but they are not"

    # correctly applies a double block card
    game.apply_drawn_card(Card(Color.YELLOW, is_single_block=False))
    assert game.players.Player_4.board_space == game.board.board_spaces.YellowSpace_17, "The current player should be on yellow space 17, but they are not"

    # successfully takes a player through a shortcut if appropriate
    for _ in range(3):
        game.change_players()

    assert game.current_player() == game.players.Player_3, "The current player should be player 3, but they are not"
    
    game.apply_drawn_card(Card(Color.ORANGE))

    assert game.players.Player_3.board_space == game.board.board_spaces.PurpleSpace_9, "Player 3 should have gone through the shortcut, but they did not"

def test_undo_turn() -> None:
    game: Game = Game()
    board_space_before: BoardSpace = game.current_player().board_space

    turn_card: Card
    for card in game.deck.cards:
        turn_card = card
        break
    
    assert game.current_player() == game.players.Player_1, "the current player should be player 1 before any turn is taken, but the aren't"
    assert turn_card not in game.discard_pile.cards, "the turn card should not be in the discard pile before a turn is taken, but it is"

    game.simulate_turn(turn_card)
    assert game.current_player() != game.players.Player_1, "taking a turn should have changed players, but it did not"
    assert game.players.Player_1.board_space != board_space_before, "taking a turn should have moved player 1, but it did not"
    assert turn_card in game.discard_pile.cards, "the turn card should be in the dicard pile, but it is not"

    game.undo_turn(board_space_before, turn_card)
    assert game.current_player() == game.players.Player_1, "undoing the turn should have made player 1 the current player again, but it did not"
    assert game.players.Player_1.board_space == board_space_before, "undoing the turn should have move player 1 back to their original space, but it did not"
    assert turn_card not in game.discard_pile.cards, "undoing the turn should have taken the turn_card out of the discard pile, but it did not"

def test_copy() -> None:
    original: Game = Game()
    nut_card: Card = original.deck.find_card("nut")
    assert nut_card in original.deck.cards, "The nut card should be in the deck, but it is not"
    assert nut_card not in original.discard_pile.cards, "The nut card should not be in the discard pile, but it is"
    original.take_turn(nut_card)
    assert nut_card not in original.deck.cards, "The nut card should not be in the deck anymore, but it is"
    assert nut_card in original.discard_pile.cards, "The nut card should be in the discard pile, but it is not"
    copy: Game = original.copy()
    assert copy != original, "The copy should not be equal to the original, but it is"
    assert copy.board != original.board, "The copy's board should not be equal to the original's board"
    assert copy.board.board_spaces.BlueSpace_0 != original.board.board_spaces.BlueSpace_0, "A single board space from the copy should not be the same as a single board space from the original, but it is"
    assert copy.board.board_spaces.BlueSpace_0.color == original.board.board_spaces.BlueSpace_0.color, "The color of a single board space from the copy should be the same as the color of a single board space from the original, but it isn't"
    assert copy.board.board_spaces.BlueSpace_0.position == original.board.board_spaces.BlueSpace_0.position, "The position of a single board space from the copy should be the same as the color of a single board space from the original, but it isn't"
    assert copy.board.board_spaces.BlueSpace_0.sticky == original.board.board_spaces.BlueSpace_0.sticky, "The sticky attribute of a single board space from the copy should be the same as the sticky attribute from the original, but it isn't"
    assert copy.board.board_spaces.BlueSpace_0.shortcut == original.board.board_spaces.BlueSpace_0.shortcut, "The shortcut attribute of a single board space from the copy should be the same as the original, but it is not"
    assert copy.board.board_spaces.BlueSpace_0.treat == original.board.board_spaces.BlueSpace_0.treat, "The treat attribute of a single board space from the original should be the same as the copy, but it isn't"
    assert copy.players.Player_1 != original.players.Player_1, "A single player from the copy should not equal a single player from the original, but it is"
    assert copy.players.Player_1.player_number == original.players.Player_1.player_number, "The player number of a single player from the original should be the same as the copy, but it isn't"
    assert copy.players.Player_1.board_space != original.players.Player_1.board_space, "The board space of a single player from the original should not be the same as the board space of a single player from the copy, but it is"
    assert copy.players.Player_1.is_current_player == original.players.Player_1.is_current_player, "The is current player attribute of a single player from the original should be the same as the is current attribute from the copy, but it isn't"
    assert copy.players.Player_1.shortcut_taken == original.players.Player_1.shortcut_taken, "The shortcut taken attribute of a single player from the original should be the same as the one from the copy, but it isn't"
    assert copy.players.Player_1.stuck_state == original.players.Player_1.stuck_state, "The stuck state of a single player from the original should be the same as the copy, but it isn't"
    assert copy.players.Player_1.board_space.color == original.players.Player_1.board_space.color, "The color of the board space of a single player from the original should be the same as the copy, but it isn't"
    assert copy.players.Player_1.board_space.position == original.players.Player_1.board_space.position, "The position of the board space of a single player from the original should be the same as the copy, but it isn't"
    assert copy.players.Player_1.board_space.sticky == original.players.Player_1.board_space.sticky, "The sticky attribute of the board space of a single player from the original should be the same as from the copy, but it isn't"
    assert copy.players.Player_1.board_space.shortcut == original.players.Player_1.board_space.shortcut, "The shortcut attribute of the board space of a single player from the copy should be the seame as that of the original, but it isn't"
    assert copy.players.Player_1.board_space.treat == original.players.Player_1.board_space.treat, "The treat attribute of the board space of a single player from the original should be the same as from the copy, but it is not"
    assert copy.discard_pile != original.discard_pile, "The discard piles of the original and copy should not the be same, but they are"
    assert nut_card not in copy.deck.cards, "The nut card should not be in the copy deck, but it is"
    assert nut_card not in copy.discard_pile.cards, "The SAME nut card should not be in the discard pile, but it is"
    for card in copy.discard_pile.cards:
        assert card.treat == Treat.NUT, "A copy of the nut card should be in the copy's discard pile, but it is not"
        assert card != nut_card, "The copy of the nut should not be the same as the original"
    assert copy.deck != original.deck, "The copy deck should not be the same as the original deck"
    