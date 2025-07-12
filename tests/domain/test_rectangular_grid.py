import pytest
from domain.rectangular_grid import RectangularGrid
from domain.position import Position

@pytest.fixture(scope='module')
def grid():
    return RectangularGrid(5, 5)

# Position validation
def test_valid_position_inside_bounds(grid):
    assert grid.is_valid_position(Position(3 ,4))

def test_valid_position_lower_bounds(grid):
    assert grid.is_valid_position(Position(0 ,0))
    
def test_valid_position_upper_bounds(grid):
    assert grid.is_valid_position(Position(5 ,5))

def test_invalid_position_out_of_bounds_x(grid):
    assert not grid.is_valid_position(Position(6, 1))

def test_invalid_position_out_of_bounds_y(grid):
    assert not grid.is_valid_position(Position(1, 6))

def test_invalid_position_negative_x(grid):
    assert not grid.is_valid_position(Position(-1, 1))

def test_invalid_position_negative_y(grid):
    assert not grid.is_valid_position(Position(1, -1))

# Constructor validation 
def test_grid_rejects_negative_x():
    with pytest.raises(ValueError):
        RectangularGrid(-5, 5)

def test_grid_rejects_negative_y():
    with pytest.raises(ValueError):
        RectangularGrid(5, -5)

def test_grid_empty():
    with pytest.raises(ValueError):
        RectangularGrid(0, 0)

def test_grid_horizontal_stripe():
    grid = RectangularGrid(5, 0)
    assert grid.is_valid_position(Position(0, 0))
    assert grid.is_valid_position(Position(5, 0))
    assert not grid.is_valid_position(Position(5, 1))

def test_grid_vertical_stripe():
    grid = RectangularGrid(0, 5)
    assert grid.is_valid_position(Position(0, 0))
    assert grid.is_valid_position(Position(0, 5))
    assert not grid.is_valid_position(Position(1, 5))