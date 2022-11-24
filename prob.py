# given a game state, calculate each player's probability of winning
from test_game import TestGame
from board_space import Color
from player import Player
from candy_land import game
from typing import Dict, Set, List
from game import Game
from board_space import BoardSpace
from card import Card
import datetime

test_game = TestGame()
test_total = {"games": 0}

def format_probability(player: Player) -> float:
    memo: Dict[str, int] = {}
    total: Dict[str, int] = {"games": 0}
    game_copy: Game = Game(game.game_state)
    player_copy: Player
    # for game_player in game.players:
    #     print(game_player.board_space)
    # print('------------------')
    for game_copy_player in game_copy.players:
        # print(game_copy_player.board_space)
        if game_copy_player.player_number == player.player_number:
            player_copy = game_copy_player

    def generate_key(discard_pile: Set[Card]) -> str:
        key_as_list: List[str] = []
        for card in discard_pile:
            is_single_block: str = str(card.is_single_block)
            color: str = card.color.name
            treat: str = str(None) if card.treat is None else card.treat.name
            id: str = f"{is_single_block}-{color}-{treat}"
            key_as_list.append(id)

        return ",".join(key_as_list)

    def win_probability(player: Player) -> int:
        key: str = generate_key(game.discard_pile.cards)
        # print('here')
        # if key in memo:
        #     if memo[key] == 1:
        #         print(memo[key])
            # print('here')
            # return memo[key]
        
        if game_copy.is_game_over():
            total["games"] += 1
            # if total["games"] == 100000:
                # print("finished 1000 games time: ", datetime.datetime.now())
                # print('finished 1000 games')

            if player.board_space.color == Color.END:
                memo[key] = 1
                # print(memo[key])
                return 1
            else:
                memo[key] = 0
                return 0

        wins: int = 0
        for card in game_copy.deck.cards:
            if card not in game.discard_pile.cards:
                board_space_before: BoardSpace = game_copy.current_player().board_space
                game_copy.simulate_turn(card)
                wins += win_probability(player)
                game_copy.undo_turn(board_space_before, card)

        memo[key] = wins
        if wins > 0:
            print(wins)
        # print(wins)
        return wins

    # print("start time: ", datetime.datetime.now())
    player_wins = win_probability(player_copy)
    # return player_wins / total["games"]


# print(format_probability(game.players.Player_1))
format_probability(game.players.Player_1)

def test_prob():
    if test_game.test_players[0].board_space.color == Color.END:
        test_total["games"] += 1
        return 1

    if test_game.test_players[1].board_space.color == Color.END:
        test_total["games"] += 1
        return 0

    wins = 0
    for card in test_game.test_deck:
        if card not in test_game.test_discard_pile:
            board_space_before = test_game.current_test_player().board_space
            test_game.take_test_turn(card)
            wins += test_prob()
            test_game.undo_test_turn(board_space_before, card)

    return wins

# print("prob: ", test_prob())
# print("total games: ", total["games"])