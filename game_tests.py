from game import Game
from player import Player
from board import *
from game_state import *
from discard_pile import DiscardPile
from card import *
from typing import Set, List
from deck import Deck

def test_new_game() -> None:
    # creating a new game without a game state, initializes the game
    # with the correct game state
    game: Game = Game()
    game_state: GameState = game.game_state

    players: GameStatePlayers = game_state.players
    discard_pile: DiscardPile = game_state.discard_pile

    correct_players: GameStatePlayers = GameStatePlayers(
        Player(1, BoardSpace(Color.START, 0), is_current_player=True),
        Player(2, BoardSpace(Color.START, 0)),
        Player(3, BoardSpace(Color.START, 0)),
        Player(4, BoardSpace(Color.START, 0)),
    )
    correct_discard_pile: DiscardPile = DiscardPile(set())

    assert has_correct_players(players, correct_players) == True, "The game state has incorrect players"
    assert has_correct_discard_pile(discard_pile, correct_discard_pile) == True, "The game state has an incorrect discard pile"

    # creating a new game with a game state, initializes the game
    # with the correct game state
    game_state = GameState(
        GameStatePlayers(
            Player(1, BoardSpace(Color.BLUE, 3)),
            Player(2, BoardSpace(Color.START, 0)),
            Player(3, TreatSpace(Treat.CANDY_CANE), is_current_player=True),
            Player(4, BoardSpace(Color.PURPLE, 15)),
        ),
        DiscardPile({
            Card(Color.PURPLE), 
            Card(Color.ORANGE, is_single_block=False), 
            TreatCard(Treat.FROST)
        })
    )
    game = Game(game_state)
    game_state = game.game_state

    players = game_state.players
    discard_pile = game_state.discard_pile

    correct_players = GameStatePlayers(
        Player(1, BoardSpace(Color.BLUE, 3)),
        Player(2, BoardSpace(Color.START, 0)),
        Player(3, TreatSpace(Treat.CANDY_CANE), is_current_player=True),
        Player(4, BoardSpace(Color.PURPLE, 15)),
    )
    correct_discard_pile = DiscardPile({
        Card(Color.PURPLE),
        Card(Color.ORANGE, is_single_block=False),
        TreatCard(Treat.FROST)
    })

    assert has_correct_players(players, correct_players) == True, "The game state has incorrect players"
    assert has_correct_discard_pile(discard_pile, correct_discard_pile) == True, "The game state has an incorrect discard pile"

def has_correct_players(players: GameStatePlayers, correct_players: GameStatePlayers) -> bool:
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
    # cards = [frost]

    cards_count: int = 0
    for card in game.deck.cards:
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

    # finds the next player even when the current player is player 4
    game = Game(GameState(
        GameStatePlayers(
            Player(1, BoardSpace(Color.BLUE, 0)),
            Player(2, BoardSpace(Color.GREEN, 5)),
            Player(3, BoardSpace(Color.ORANGE, 9)),
            Player(4, BoardSpace(Color.PURPLE, 13), is_current_player=True)
        ),
        DiscardPile()
    ))

    assert game.next_player() == game.players.Player_1, "player 1 should be the next player, but is not"
    assert game.next_player() != game.players.Player_2, "player 2 should not be the next player"
    assert game.next_player() != game.players.Player_3, "player 3 should not be the next player"
    assert game.next_player() != game.players.Player_4, "player 4 should not be the next player"

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
    # if you create a game without passing in a game state, all of the players'
    # board spaces should be the actual board spaces on the board
    game: Game = Game()
    for player in game.players:
        assert player.board_space in game.board.board_spaces, "A player's board space was not found on the board for a game with an empty game state"

    # if you create a game by passing in a game state, all of the players'
    # board spaces should be the actual board spaces on the board
    game = Game(GameState(
        GameStatePlayers(
            Player(1, BoardSpace(Color.GREEN, 2)),
            Player(2, BoardSpace(Color.YELLOW, 7, sticky=True)),
            Player(3, TreatSpace(Treat.NUT)),
            Player(4, BoardSpace(Color.PURPLE, 8), is_current_player=True)
        ),
        DiscardPile()
    ))

    for player in game.players:
        assert player.board_space in game.board.board_spaces, "A player's board space was not found on the board for a game with a given game state"

def test_change_players() -> None:
    # if player 1 is the current player, when you change players, player 2 should be the current player
    game: Game = Game()
    players: GameStatePlayers = game.players
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
    game.move_curr_player_to_treat(Treat.PLUMB)
    for _ in range(4):
        game.move_curr_player_to_next_color(Color.PURPLE)

    assert player.board_space == game.board.board_spaces.GumdropPass, "The player should be on gumdrop pass, but they are not"
    game.take_curr_player_through_shortcut()

    assert player.board_space == game.board.board_spaces.PurpleSpace_7, "The player should be on purple space 7, but they are not"

def test_apply_drawn_card() -> None:
    game: Game = Game(GameState(
        GameStatePlayers(
            Player(1, TreatSpace(Treat.CANDY_CANE)),
            Player(2, BoardSpace(Color.RED, 13)),
            Player(3, BoardSpace(Color.START, 0), is_current_player=False),
            Player(4, BoardSpace(Color.RED, 19, sticky=True), is_current_player=True)
        ),
        DiscardPile({ 
            Card(Color.GREEN), 
            Card(Color.RED, is_single_block=False), 
            Card(Color.GREEN, is_single_block=True), 
            Card(Color.GREEN, is_single_block=False),
            TreatCard(Treat.GUMDROP),
            TreatCard(Treat.NUT),
        })
    ))

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