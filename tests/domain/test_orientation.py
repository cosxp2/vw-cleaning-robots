import pytest
from domain.orientation import Orientation

@pytest.mark.parametrize(
    ('initial', 'final'),
    [
        (Orientation.NORTH, Orientation.WEST),
        (Orientation.WEST, Orientation.SOUTH),
        (Orientation.SOUTH, Orientation.EAST),
        (Orientation.EAST, Orientation.NORTH),
    ]
)
def test_turn_left(initial, final):
    assert initial.turn_left() == final

@pytest.mark.parametrize(
    ('initial', 'final'),
    [
        (Orientation.NORTH, Orientation.EAST),
        (Orientation.EAST, Orientation.SOUTH),
        (Orientation.SOUTH, Orientation.WEST),
        (Orientation.WEST, Orientation.NORTH),
    ]
)
def test_turn_right(initial, final):
    assert initial.turn_right() == final
    
@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('N', Orientation.NORTH),
        ('W', Orientation.WEST),
        ('S', Orientation.SOUTH),
        ('E', Orientation.EAST),
        ('e', Orientation.EAST),
    ]
)
def test_valid_orientation_input(input, expected):
    assert Orientation.from_str(input) == expected

@pytest.mark.parametrize(
    'input', ['X', '-1', '', '   ']
)  
def test_invalid_orientation_input(input):
    with pytest.raises(ValueError):
        Orientation.from_str(input)