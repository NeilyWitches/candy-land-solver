# The Candy Land Solver!
## play candy land with four players and see each player's probability of winning at every turn!
### you can play a fresh game by simply running candy_land.py
### the progam is meant to be used alongside a real game of candy land
- draw a card in real life
- input the card when prompted
- see each player's probability of winning
- if you want to fast-forward to a point in the middle of a game you'll need to tell the program what state the game is in by
    - entering each player's position on the board
    - entering every card in the discard pile
    - telling the program whose turn it is at the moment
    - do this by modifying candy_land.py (see below on how exactly to do this)
### you can play a game from any given game state by modifying candy_land.py
#### `Game` takes in a `GameState` as an optional argument
- a `GameState` accepts 2 arguments:
    - `GameStatePlayers`, a named tuple of `Player` objects, which accept 2 arguments and 1 optional arugment:
        - player_number: `int`, this dictates the order the players go in (for simplicity you can give `1` to `Player_1`, `2` to `Player_2`, etc)
        - board_space: 
            - `BoardSpace`, for normal colored spaces, which accepts 2 arguments and 1 optional argument:
                - color: `Color` a color from an `Enum`:
                    1. `Color.START`
                    2. `Color.RED`
                    3. `Color.PURPLE`
                    4. `Color.YELLOW`
                    5. `Color.BLUE`
                    6. `Color.ORANGE`
                    7. `Color.GREEN`
                    8. `Color.PINK`
                    9. `Color.END`
                - position: `int`, Zero-based numbering of color spaces in the order they appear from the start menu (see `board.py`, `generate_board`)
                - sticky (optional): `bool`, if the space is a sticky space, set to `True`
            - `ShortcutSpace`, which accepts 1 arugment, a `Shortcut` for the two board spaces that contain the shortcuts:
                - `Shortcut.RAINBOW_TRAIL`
                - `Shortcut.GUMDROP_PASS`
            - `TreatSpace`, which accepts 1 argument, a `Treat` for the 6 board spaces that are treats:
                - `Treat.PLUM`
                - `Treat.CANDY_CANE`
                - `Treat.GUMDROP`
                - `Treat.LOLLIPOP`
                - `Treat.NUT`
                - `Treat.FROST`
        - is_current_player: `bool` exactly 1 player **must** have this optional boolean set to `True` so the game knows whose turn it is
    - `DiscardPile`, takes in 1 optional argument, a set of `cards`
        - `Card`, which accepts 1 argument and 1 optional argument:
            - color (the same as the colors found in `board_space` excluding `Color.START`, `Color.END`, and `Color.PINK`)
            - is_single_block (optional): `bool`, set to `False` if the card has 2 squares instead of 1
        - `TreatCard`, which accepts 1 argument, a `Treat` exactly the same as `TreatSpace`
- An example of a `Game` with a valid game state:
```
Game(GameState(
    GameStatePlayers(
        Player(1, BoardSpace(Color.GREEN, 5)),
        Player(2, BoardSpace(Color.YELLOW, 7, sticky=True)),
        Player(3, TreatSpace(Treat.FROST)),
        Player(4, BoardSpace(Color.RED, 20), is_current_player=True),
    ),
    DiscardPile({
        Card(Color.BLUE),
        Card(Color.GREEN, is_single_block=False),
        TreatCard(Treat.GUMDROP),
    })
))
``` 