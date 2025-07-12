import pytest
from domain.position import Position
from domain.orientation import Orientation

@pytest.mark.parametrize(
    ('initial', 'orientation', 'final'),
    [
        (Position(1, 2), Orientation.NORTH, Position(1, 3)),
        (Position(5, 5), Orientation.SOUTH, Position(5, 4)),
        (Position(0, 0), Orientation.EAST,  Position(1, 0)),
        (Position(2, 2), Orientation.WEST,  Position(1, 2)),
    ]
)
def test_position_move(initial, orientation, final):
    assert initial.move(orientation) == final