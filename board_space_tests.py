from board_space import *

def test_copy() -> None:
    # works for an ordinary board space
    original: BoardSpace = BoardSpace(Color.YELLOW, 7, sticky=True)
    copy: BoardSpace = original.copy()
    assert original != copy, "The original should not be equal to the copy, but it is"
    assert original.color == copy.color, "The original's color should be the same as the copy's color, but it isn't"
    assert original.position == copy.position, "The original's position should be the same as the copy's position, but it isn't"
    assert original.sticky == copy.sticky, "The original's sticky should be the same as the copy's sticky, but it isn't"
    assert original.treat == copy.treat, "The original's treart should be the same as the copy's treat"

    # works for a shortcut space
    original = ShortcutSpace(Shortcut.GUMDROP_PASS)
    copy = original.copy()
    assert original != copy, "The original should not be equal to the copy, but it is"
    assert original.color == copy.color, "The original's color should be the same as the copy's color, but it isn't"
    assert original.position == copy.position, "The original's position should be the same as the copy's position, but it isn't"
    assert original.sticky == copy.sticky, "The original's sticky should be the same as the copy's sticky, but it isn't"
    assert original.treat == copy.treat, "The original's treart should be the same as the copy's treat"

    # works for a treat space
    original = TreatSpace(Treat.CANDY_CANE)
    copy = original.copy()
    assert original != copy, "The original should not be equal to the copy, but it is"
    assert original.color == copy.color, "The original's color should be the same as the copy's color, but it isn't"
    assert original.position == copy.position, "The original's position should be the same as the copy's position, but it isn't"
    assert original.sticky == copy.sticky, "The original's sticky should be the same as the copy's sticky, but it isn't"
    assert original.treat == copy.treat, "The original's treart should be the same as the copy's treat"