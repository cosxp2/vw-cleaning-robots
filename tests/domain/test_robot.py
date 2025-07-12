import pytest
from domain.robot import Robot
from domain.rectangular_grid import RectangularGrid
from domain.position import Position
from domain.orientation import Orientation
from domain.command import Command 

@pytest.fixture(scope='module')
def grid():
    return RectangularGrid(5, 5)

@pytest.fixture(scope='function')
def robot():
    return Robot(Position(1, 2), Orientation.NORTH)

def test_execute_move_forward(robot, grid):
    robot.execute(Command.MOVE, grid)
    assert robot.position == Position(1, 3)
    assert robot.orientation == Orientation.NORTH

def test_execute_turn_left(robot, grid):
    robot.execute(Command.LEFT, grid)
    assert robot.orientation == Orientation.WEST

def test_execute_turn_right(robot, grid):
    robot.execute(Command.RIGHT, grid)
    assert robot.orientation == Orientation.EAST

def test_execute_sequence(robot, grid):
    robot.execute_all([
        Command.LEFT,
        Command.MOVE,
        Command.LEFT,
        Command.MOVE,
        Command.LEFT,
        Command.MOVE,
        Command.LEFT,
        Command.MOVE,
        Command.MOVE
    ], grid)
    assert robot.position == Position(1, 3)
    assert robot.orientation == Orientation.NORTH


@pytest.mark.parametrize(
    ("position", "orientation"),
    [
        (Position(0, 5), Orientation.NORTH),  # top edge
        (Position(0, 0), Orientation.SOUTH),  # bottom edge
        (Position(5, 0), Orientation.EAST),   # right edge
        (Position(0, 0), Orientation.WEST),   # lfet edge
    ]
)
def test_robot_does_not_move_out_of_bounds(position, orientation, grid):
    robot = Robot(position, orientation)
    robot.execute(Command.MOVE, grid)
    assert robot.position == position  # should not move
    assert robot.orientation == orientation  # should not rotate

def test_robot_rejects_invalid_command(robot, grid):
    class FakeCommand:
        pass 

    with pytest.raises(ValueError):
        robot.execute(FakeCommand(), grid)
